package edu.usc.smakwana.crawler.twitter.services;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import twitter4j.Query;
import twitter4j.QueryResult;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;

public class Test {
	
	public static void main(String args[]) {
		
		ConfigurationBuilder cb = new ConfigurationBuilder();
	    cb.setOAuthConsumerKey("79vyiKl9rYg5BgnD9FM7Y2kqy");
	    cb.setOAuthConsumerSecret("jnH8aseVgSdAT4TGGRKBmvr23hoBb7mxQu82JtTtGy66oNY56w");
	    cb.setOAuthAccessToken("282542631-HYYwFLd1mQDYGAFU68AZO9NIgvwF0r9xpo3ExHUx");
	    cb.setOAuthAccessTokenSecret("yzBusFtCZuV9bOSLLxa6IFNilg5EuECDQ5gwxqgM1MZtG");

	    Twitter twitter = new TwitterFactory(cb.build()).getInstance();
	    List<Status> statuses = new ArrayList();
		
		Query query  = new Query();
	    query.setLang("hi");
	    //query.setSince("2017-03-01");
	    //query.setUntil("2017-04-01");
	    query.setQuery("from:narendramodi");
	    
	    try {
	    	QueryResult queryResult = twitter.search(query);
	    	statuses.addAll(queryResult.getTweets());
	    	
	    	if (queryResult.hasNext()){
	    		query = queryResult.nextQuery();
	    		queryResult = twitter.search(query);
	    		statuses.addAll(queryResult.getTweets());
	    	}
		} catch (TwitterException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	    
	    
	    System.out.println("Total: "+statuses.size());
	    
	    Iterator<Status> iterator = statuses.iterator();
	    
	    while (iterator.hasNext()) {
			Status status = (Status) iterator.next();
			System.out.println(status.getUser().getScreenName() + " ---" + status.getText() );
			
		}
		
	}

}
