package summerschool.sentiment;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

import org.json.simple.parser.ContainerFactory;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.jsoup.Jsoup;

public class JsonRead {

	public static void parse(String jsonText, PrintWriter pw) {
		JSONParser parser = new JSONParser();
		ContainerFactory containerFactory = new ContainerFactory() {
			public List creatArrayContainer() {
				return new LinkedList();
			}

			public Map createObjectContainer() {
				return new LinkedHashMap();
			}

		};

		try {
			Map json = (Map) parser.parse(jsonText, containerFactory);
			Iterator iter = json.entrySet().iterator();
			Object id = null;
			int sentiment = 0;
			while (iter.hasNext()) {
				Map.Entry entry = (Map.Entry) iter.next();

				if (entry.getKey().equals("content")) {
					String content = (String) entry.getValue();
					content = Jsoup.parse(content).text();
					sentiment = NLP.findSentiment(content);
				} else if (entry.getKey().equals("_id")) {
					id = entry.getValue();
				}

			}
			pw.println(id + " " + sentiment);
			pw.flush();
		} catch (ParseException pe) {
			System.out.println(pe);
			pe.printStackTrace();
			pw.close();
		} finally {
		}
	}

	public static void main(String[] args) throws IOException {
		NLP.init();
		BufferedReader br = new BufferedReader(new FileReader("D:\\Dataset\\India_Election\\Narendra_Modi\\tweets.txt"));
		//Scanner fi = new Scanner(new File("D:\\Dataset\\India_Election\\Narendra_Modi\\tweets.txt"));
		PrintWriter pw = new PrintWriter("output.txt");
		int counter = 0;
		String line = br.readLine();
		while (line!= null) {
			StringBuilder sb = new StringBuilder();
			if(counter%10 == 0)
				System.out.println("TWEET >> " + counter);
			parse(line, pw);
			counter++;
			line = br.readLine();
		}
	}
}
