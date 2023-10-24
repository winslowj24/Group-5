import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class datetime_convert {
    public static void main(String[] args) {
        // Create a string containing date and time
        String dateStr = "2022-03-17 10:45:30";

        // Create DateTimeFormatter object with string
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        // New date object with date string parsed
        LocalDateTime dateObj = LocalDateTime.parse(dateStr, formatter);

        // Create new string from the date object
        String formattedDate = dateObj.format(DateTimeFormatter.ofPattern("MM/dd/yyyy HH:mm:ss"));

        // Print the new string
        System.out.println(formattedDate);
    }
}
