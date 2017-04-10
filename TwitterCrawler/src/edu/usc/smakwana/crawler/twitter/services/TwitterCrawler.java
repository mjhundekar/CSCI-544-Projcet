package edu.usc.smakwana.crawler.twitter.services;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

import twitter4j.FilterQuery;
import twitter4j.HashtagEntity;
import twitter4j.StallWarning;
import twitter4j.Status;
import twitter4j.StatusDeletionNotice;
import twitter4j.StatusListener;
import twitter4j.TwitterStream;
import twitter4j.TwitterStreamFactory;
import twitter4j.conf.ConfigurationBuilder;

public class TwitterCrawler extends TimerTask implements StatusListener{
	private TwitterStream twitterStream;
	private PrintWriter printWriter = null;

	
	public void streamInitialization(){
		ConfigurationBuilder config = new ConfigurationBuilder();
	    config.setOAuthConsumerKey("");
	    config.setOAuthConsumerSecret("");
	    config.setOAuthAccessToken("");
	    config.setOAuthAccessTokenSecret("");

	    twitterStream = new TwitterStreamFactory(config.build()).getInstance();
	    twitterStream.addListener(this);
	}
	
	public void setFiltersToStream(TwitterStream twitterStream){
		
		FilterQuery filterQuery = new FilterQuery();
		double box[][] = {{65.0, 6.0}, {97.35, 35.95}};
	    filterQuery.locations(box);
	    filterQuery.language("hi");

	    twitterStream.filter(filterQuery);
	}


	@Override
	public void run() {
		
		if (printWriter != null){
			printWriter.close();
		}
		
		String timeStamp = new SimpleDateFormat("yyyy-MM-dd-HH-mm-ss").format(new Date());
		try {
			printWriter = new PrintWriter(timeStamp + ".txt","utf-8");
		} catch (FileNotFoundException | UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		
	}


	@Override
	public void onException(Exception arg0) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void onDeletionNotice(StatusDeletionNotice arg0) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void onScrubGeo(long arg0, long arg1) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void onStallWarning(StallWarning arg0) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void onStatus(Status status) {
		printWriter.println(status.getUser().getScreenName() + " :::: " + status.getText() + " :::: " + status.getGeoLocation() +" :::: "+ status.getCreatedAt().toString() + " :::: "+ getHashTags(status.getHashtagEntities()));
		System.out.println(status.getText());
	}


	@Override
	public void onTrackLimitationNotice(int arg0) {
		// TODO Auto-generated method stub
		
	}


	public TwitterStream getTwitterStream() {
		return twitterStream;
	}


	public void setTwitterStream(TwitterStream twitterStream) {
		this.twitterStream = twitterStream;
	}
	
	
	public String getHashTags (HashtagEntity[] hashtagEntities){
		String result = "";
		for (int i = 0; i < hashtagEntities.length; i++) {
			result += "#" + hashtagEntities[i].getText() ;
		}
		return result;
	}
	
	public static void main(String args[]){
		
		TwitterCrawler twitterCrawler = new TwitterCrawler();
		Timer timer = new Timer();
		timer.schedule(twitterCrawler,0,3600000);
		twitterCrawler.streamInitialization();
		twitterCrawler.setFiltersToStream(twitterCrawler.getTwitterStream());
	}

}
