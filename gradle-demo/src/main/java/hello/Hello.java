package hello;

import org.joda.time.LocalTime;

public class Hello {
    public static void main(String args[]){

        LocalTime localTime = new LocalTime();
        System.out.println("currnt time is: " + localTime );

        Greeter greeter = new Greeter();
        System.out.println(greeter.greet_now());
    }
}

