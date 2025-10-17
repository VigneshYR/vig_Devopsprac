package com.mypractice.helloworldapp;

/**
 * Hello world!
 */
public class Helloworldapp {

    private static final String MESSAGE = "Hello World!";

    public App() {}

    public static void main(String[] args) {
        System.out.println(MESSAGE);
    }

    public String getMessage() {
        return MESSAGE;
    }
}