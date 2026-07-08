package org.athomeprojects.base;

import java.io.File;
import java.net.URL;

// Spike stub: swisseph 的 swi_fopen 用 FileIO.getURL 把文件名转成 URL 再打开。
// 本地星历文件直接返回 File.toURI().toURL()。
public class FileIO {
    static public String getFileName(String file_name) { return file_name; }
    static public URL getURL(String file_name) {
        try {
            return new File(file_name).toURI().toURL();
        } catch (Exception e) {
            return null;
        }
    }
    static public void setProgress(int val) {}
}

