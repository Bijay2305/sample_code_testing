import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class ImageUploader {
    public static void main(String[] args) {
        String apiUrl = "http://localhost:5000/upload";
        String imagePath = "/path/to/image.jpg";

        try {
            // Read the image file into a byte array
            Path path = Paths.get(imagePath);
            byte[] imageBytes = Files.readAllBytes(path);

            // Create a URL object with the API URL
            URL url = new URL(apiUrl);

            // Open a connection to the URL
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);

            // Set the request headers
            connection.setRequestProperty("Content-Type", "image/jpeg");
            connection.setRequestProperty("Content-Length", String.valueOf(imageBytes.length));

            // Write the image data to the request body
            OutputStream outputStream = connection.getOutputStream();
            outputStream.write(imageBytes);
            outputStream.close();

            // Get the response from the API
            int responseCode = connection.getResponseCode();
            BufferedReader reader;
            if (responseCode == HttpURLConnection.HTTP_OK) {
                reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            } else {
                reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            }

            // Read the response line by line
            String line;
            StringBuilder response = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            // Print the response
            System.out.println(response.toString());

            // Close the connection
            connection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
