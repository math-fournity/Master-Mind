import org.athomeprojects.swisseph.SweConst;
import org.athomeprojects.swisseph.SweDate;
import org.athomeprojects.swisseph.SwissEph;

/**
 * SpikeChart2: 扩展SpikeChart，额外输出ASC/MC/宫位。
 * 用法: java -cp build/spike SpikeChart2 year month day hour_ut longitude latitude
 */
public class SpikeChart2 {
    public static void main(String[] args) throws Exception {
        if (args.length < 6) {
            System.err.println("Usage: SpikeChart2 year month day hour_ut longitude latitude");
            System.exit(1);
        }
        int year = Integer.parseInt(args[0]);
        int month = Integer.parseInt(args[1]);
        int day = Integer.parseInt(args[2]);
        double hourUt = Double.parseDouble(args[3]);
        double lon = Double.parseDouble(args[4]);
        double lat = Double.parseDouble(args[5]);

        double jd = SweDate.getJulDay(year, month, day, hourUt);
        SwissEph se = new SwissEph();
        se.swe_set_ephe_path("ephe");
        se.swe_set_sid_mode(SweConst.SE_SIDM_LAHIRI, 0.0, 0.0);
        int flag = SweConst.SEFLG_SWIEPH | SweConst.SEFLG_SIDEREAL | SweConst.SEFLG_SPEED;

        StringBuilder sb = new StringBuilder();
        sb.append("{");

        // input
        sb.append("\"input\":{");
        sb.append("\"date_ut\":\"").append(String.format("%04d-%02d-%02dT%07.4f", year, month, day, hourUt)).append("\",");
        sb.append("\"jd\":").append(jd).append(",");
        sb.append("\"lon\":").append(lon).append(",");
        sb.append("\"lat\":").append(lat);
        sb.append("},");

        // bodies
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

        sb.append("\"bodies\":{");
        double[] xx = new double[6];
        StringBuffer serr = new StringBuffer();
        double sunLon = 0;
        for (int i = 0; i < planets.length; i++) {
            int ret = se.swe_calc_ut(jd, planets[i], flag, xx, serr);
            if (i > 0) sb.append(",");
            sb.append("\"").append(names[i]).append("\":{");
            sb.append("\"ret\":").append(ret);
            if (ret >= 0) {
                sb.append(",\"lon\":").append(round(xx[0], 6));
                sb.append(",\"lat\":").append(round(xx[1], 6));
                sb.append(",\"lon_speed\":").append(round(xx[3], 6));
                if (i == 0) sunLon = xx[0];
            } else {
                sb.append(",\"error\":\"").append(serr.toString().replace("\"","'")).append("\"");
            }
            sb.append("}");
        }
        sb.append("},");

        // houses
        double[] cusps = new double[13];
        double[] ascmc = new double[10];
        int hflag = SweConst.SEFLG_SIDEREAL;
        se.swe_houses(jd, hflag, lat, lon, 'P', cusps, ascmc);

        sb.append("\"houses\":{");
        sb.append("\"asc\":").append(round(ascmc[0], 6)).append(",");
        sb.append("\"mc\":").append(round(ascmc[1], 6)).append(",");
        sb.append("\"armc\":").append(round(ascmc[2], 6)).append(",");
        sb.append("\"cusps\":[");
        for (int i = 0; i < 12; i++) {
            if (i > 0) sb.append(",");
            sb.append(round(cusps[i+1], 6));
        }
        sb.append("]");
        sb.append("},");

        // ayanamsa
        double ayanamsa = se.swe_get_ayanamsa_ut(jd);
        sb.append("\"ayanamsa\":").append(round(ayanamsa, 6));

        sb.append("}");
        System.out.println(sb.toString());
    }

    static double round(double v, int d) {
        double f = Math.pow(10, d);
        return Math.round(v * f) / f;
    }
}
