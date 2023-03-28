package service;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.FileWriter;
 public class OutputService {
    public static void out(Object o){
        ObjectMapper objectMapper = new ObjectMapper();
        try (FileWriter fileWriter = new FileWriter("output.json")) {
            fileWriter.write(objectMapper.writeValueAsString(o));
        }catch (Exception e){
            System.out.println(e.getMessage());
        }
    }
}
