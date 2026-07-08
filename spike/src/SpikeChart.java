import org.athomeprojects.swisseph.SweConst;
import org.athomeprojects.swisseph.SweDate;
import org.athomeprojects.swisseph.SwissEph;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Spike: 验证 swisseph 核心能否脱离 GUI 独立运行。
 * 输入: year month day hour(UT, 小数) longitude latitude
 * 输出: JSON, 含七政四余主要天体的恒星黄道经度。
 *
 * 用法:
 *   java -cp build/spike SpikeChart 1990 5 15 3.5 116.4 39.9
 */
public class SpikeChart {
    public static void main(String[] args) throws Exception {
        if (args.length < 5) {
            System.err.println("Usage: SpikeChart year month day hour_ut longitude latitude");
            System.exit(1);
        }
        int year = Integer.parseInt(args[0]);
        int month = Integer.parseInt(args[1]);
        int day = Integer.parseInt(args[2]);
        double hourUt = Double.parseDouble(args[3]);
        double lon = Double.parseDouble(args[4]);
        double lat = args.length > 5 ? Double.parseDouble(args[5]) : 0.0;

        // 1. 儒略日
        double jd = SweDate.getJulDay(year, month, day, hourUt);

        // 2. SwissEph 实例 + 星历路径
        SwissEph se = new SwissEph();
        se.swe_set_ephe_path("ephe");

        // 3. 恒星黄道（七政四余用恒星黄道）+ Lahiri ayanamsa
        //    MOIRA 的 sidereal_systems 里默认第一项是 SE_SIDM_FAGAN_BRADLEY,
        //    七政四余传统用 Lahiri，这里先输出 Lahiri。
        se.swe_set_sid_mode(SweConst.SE_SIDM_LAHIRI, 0.0, 0.0);
        int flag = SweConst.SEFLG_SWIEPH | SweConst.SEFLG_SIDEREAL | SweConst.SEFLG_SPEED;

        // 4. 天体列表：七政（日月水金火木土）+ 四余（罗睺=真北交点, 计都=真南交点, 紫炁=远地点, 月孛= osculating apog）
        int[] planets = {
            SweConst.SE_SUN, SweConst.SE_MOON, SweConst.SE_MERCURY, SweConst.SE_VENUS,
            SweConst.SE_MARS, SweConst.SE_JUPITER, SweConst.SE_SATURN,
            SweConst.SE_TRUE_NODE, SweConst.SE_MEAN_APOG, SweConst.SE_OSCU_APOG
        };
        String[] names = {
            "sun", "moon", "mercury", "venus",
            "mars", "jupiter", "saturn",
            "true_node_rohuo", "mean_apog_ziqi", "oscu_apog_yuebei"
        };

        Map<String, Object> root = new LinkedHashMap<>();
        Map<String, Object> input = new LinkedHashMap<>();
        input.put("date_ut", String.format("%04d-%02d-%02dT%07.4f", year, month, day, hourUt));
        input.put("jd", jd);
        input.put("lon", lon);
        input.put("lat", lat);
        input.put("ayanamsa", "Lahiri");
        input.put("frame", "sidereal");
        root.put("input", input);

        Map<String, Object> bodies = new LinkedHashMap<>();
        double[] xx = new double[6];
        StringBuffer serr = new StringBuffer();
        for (int i = 0; i < planets.length; i++) {
            int ret = se.swe_calc_ut(jd, planets[i], flag, xx, serr);
            Map<String, Object> body = new LinkedHashMap<>();
            body.put("ret", ret);
            if (ret >= 0) {
                body.put("lon", round(xx[0], 6));
                body.put("lat", round(xx[1], 6));
                body.put("dist", round(xx[2], 8));
                body.put("lon_speed", round(xx[3], 6));
                body.put("lat_speed", round(xx[4], 6));
                body.put("dist_speed", round(xx[5], 8));
            } else {
                body.put("error", "swe_calc_ut ret=" + ret + " serr=" + serr.toString());
            }
            bodies.put(names[i], body);
        }
        root.put("bodies", bodies);

        // 5. 输出 JSON（手工拼接，spike 不引入 JSON 库）
        System.out.println(toJson(root));
        se.swe_close();
    }

    private static double round(double v, int d) {
        double p = Math.pow(10, d);
        return Math.round(v * p) / p;
    }

    // 极简 JSON 序列化
    private static String toJson(Map<String, Object> m) {
        StringBuilder sb = new StringBuilder("{");
        int i = 0;
        for (Map.Entry<String, Object> e : m.entrySet()) {
            if (i++ > 0) sb.append(",");
            sb.append(jsonStr(e.getKey())).append(":").append(jsonVal(e.getValue()));
        }
        return sb.append("}").toString();
    }

    private static String jsonVal(Object v) {
        if (v instanceof Map) return toJson((Map<String, Object>) v);
        if (v instanceof String) return jsonStr((String) v);
        if (v instanceof Double || v instanceof Float) return String.valueOf(v);
        if (v instanceof Number) return String.valueOf(v);
        return jsonStr(String.valueOf(v));
    }

    private static String jsonStr(String s) {
        return "\"" + s.replace("\\", "\\\\").replace("\"", "\\\"") + "\"";
    }
}
