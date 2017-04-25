package com.nlp.transliteration.services;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

import com.nlp.transliteration.engine.TransliterationEngine;

public class TransliterateService {
	
	public static void main(String args[]) throws IOException{
		TransliterationEngine transliterationEngine = new TransliterationEngine();
		
		File workingDirectory = new File("F:\\USCSem3\\NLP\\NLPProjectResources\\CleanTweets");
		File outputDirectory = new File("F:\\USCSem3\\NLP\\NLPProjectResources\\TransliteratedTweets");
		FileWriter fw;
		BufferedReader br;
		File[] listOfFiles = workingDirectory.listFiles();

	    for (int i = 0; i < listOfFiles.length; i++) {
	    	br = new BufferedReader(new FileReader(new File(listOfFiles[i].getAbsolutePath())));
	    	fw = new FileWriter(new File(outputDirectory + "\\" + listOfFiles[i].getName()));
	    	String line = "";
	    	while ( (line = br.readLine())!= null){
	    		fw.write(transliterationEngine.transliterate(line) + "\n");
	    	}
	    	br.close();
	    	fw.close();
	    	System.out.println("Transliterating " + listOfFiles[i].getName());
	    }
		
	}

}
