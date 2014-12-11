package summerschool.sentiment;

import java.io.IOException;
import java.util.Properties;

import org.ejml.simple.SimpleMatrix;

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.neural.rnn.RNNCoreAnnotations;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.sentiment.SentimentCoreAnnotations;
import edu.stanford.nlp.trees.Tree;
import edu.stanford.nlp.util.CoreMap;

class NLP {
	static StanfordCoreNLP pipeline;

	public static void init() {
		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, parse, sentiment");
		pipeline = new StanfordCoreNLP(props);
	}

	public static int findSentiment(String tweet) {
		int mainSentiment = 0;
		if (tweet != null && tweet.length() > 0) {
			Annotation annotation = pipeline.process(tweet);
			int sentiment = 0;
			for (CoreMap sentence : annotation
					.get(CoreAnnotations.SentencesAnnotation.class)) {
				Tree tree = sentence
						.get(SentimentCoreAnnotations.AnnotatedTree.class);
				Object obj = sentence
						.get(SentimentCoreAnnotations.ClassName.class);
				SimpleMatrix vector = RNNCoreAnnotations.getPredictions(tree);
				double max=0;
				int s=0;
				for (int i = 0; i < vector.getNumElements(); ++i) {
					if(vector.get(i)>max){
						s=i;
						max=vector.get(i);
					}
				}
				mainSentiment=s;
			}
		}
		return mainSentiment;
	}
}

public class App {

	public static void main(String[] args) throws IOException {

		// SentimentPipeline.main(args);
		NLP.init();
		System.out.println(NLP.findSentiment(" "));
	}
}
