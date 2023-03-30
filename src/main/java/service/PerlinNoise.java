package service;

import java.util.Random;

public class PerlinNoise {
    private static double blending(double t) {
        return 6 * Math.pow(t, 5) - 15 * Math.pow(t, 4) + 10 * Math.pow(t, 3);
    }
    public static double[][] noise(int pixel, double frequency) {
        int unit = pixel * 100;
        double[][] matrix = new double[(int) Math.ceil(10 * frequency) + 2][(int) Math.ceil(10 * frequency) + 2];
        Random rand = new Random();
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[i][j] = (rand.nextDouble() * 2 - 1);
            }
        }

        double[] xArray = new double[unit];
        double[] yArray = new double[unit];
        for (int i = 0; i < unit; i++) {
            xArray[i] = i * 10.0 / unit;
            yArray[i] = i * 10.0 / unit;
        }

        double[][] Z = new double[unit][unit];
        for (int i = 0; i < xArray.length; i++) {
            for (int j = 0; j < yArray.length; j++) {
                int x1 = (int) Math.floor(xArray[i] * frequency);
                int x2 = (int) Math.floor(xArray[i] * frequency + 1);
                int y1 = (int) Math.floor(yArray[j] * frequency);
                int y2 = (int) Math.floor(yArray[j] * frequency + 1);

                double a = blending(x2 - xArray[i] * frequency) * matrix[x1][y1] + blending(xArray[i] * frequency - x1) * matrix[x2][y1];
                double b = blending(x2 - xArray[i] * frequency) * matrix[x1][y2] + blending(xArray[i] * frequency - x1) * matrix[x2][y2];

                Z[i][j] = blending(y2 - yArray[j] * frequency) * a + blending(yArray[j] * frequency - y1) * b;
                Z[i][j]   = Math.round( Z[i][j]  * 1000.0) / 1000.0;
            }
        }

        if (pixel == 1) {
            return Z;
        } else {
            double[][] resized = new double[100][100];
            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    resized[i][j] = Z[i * pixel][j * pixel];
                }
            }
            return resized;
        }
    }









}
