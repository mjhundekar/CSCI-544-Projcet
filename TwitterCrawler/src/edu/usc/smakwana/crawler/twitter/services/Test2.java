package edu.usc.smakwana.crawler.twitter.services;

import java.util.Arrays;

import twitter4j.FilterQuery;
import twitter4j.HashtagEntity;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

public class Test2 {

	public static void main(String[] args) {
		
		   StatusListener listener = new StatusListener(){
		        public void onStatus(Status status) {

		        	System.out.println(status.getUser().getScreenName() + " :::: " + status.getText() + " :::: " + status.getGeoLocation() +" :::: "+ status.getCreatedAt().toString() + " :::: "+ getHashTags(status.getHashtagEntities()));
		        }
		        public void onDeletionNotice(StatusDeletionNotice statusDeletionNotice) {}
		        public void onTrackLimitationNotice(int numberOfLimitedStatuses) {}
		        public void onException(Exception ex) {
		            ex.printStackTrace();
		        }
		        public void onScrubGeo(long arg0, long arg1) {

		        }
		        public void onStallWarning(StallWarning arg0) {

		        }
		    };
		    
		    

		    ConfigurationBuilder config = new ConfigurationBuilder();
		    config.setOAuthConsumerKey("79vyiKl9rYg5BgnD9FM7Y2kqy");
		    config.setOAuthConsumerSecret("jnH8aseVgSdAT4TGGRKBmvr23hoBb7mxQu82JtTtGy66oNY56w");
		    config.setOAuthAccessToken("282542631-HYYwFLd1mQDYGAFU68AZO9NIgvwF0r9xpo3ExHUx");
		    config.setOAuthAccessTokenSecret("yzBusFtCZuV9bOSLLxa6IFNilg5EuECDQ5gwxqgM1MZtG");

		    TwitterStream twitterStream = new TwitterStreamFactory(config.build()).getInstance();
		    twitterStream.addListener(listener);
		    FilterQuery query = new FilterQuery();
		    // New Delhi India
		    double lat = 28.6;
		    double lon = 77.2;

		    double lon1 = lon - .5;
		    double lon2 = lon + .5;
		    double lat1 = lat - .5;
		    double lat2 = lat + .5;

		    double box[][] = {{65.0, 6.0}, {97.35, 35.95}};

		    query.locations(box);
		    query.language("hi");

		    twitterStream.filter(query);

	}
	
	public static String getHashTags (HashtagEntity[] hashtagEntities){
		String result = "";
		for (int i = 0; i < hashtagEntities.length; i++) {
			result += "#" + hashtagEntities[i].getText() ;
		}
		return result;
	}
	
	

}
