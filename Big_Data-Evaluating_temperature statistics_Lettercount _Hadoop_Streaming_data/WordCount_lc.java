//Assignment Objective-letter and count 
import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount_lc {
    //WordCount class
    public static void main(String[] args) throws Exception {
        
        if (args.length != 2) {
            System.err.println("Usage:WordCount<input><output>");
            System.exit(-1);
        }
        Job job = Job.getInstance();
        job.setJarByClass(WordCount_lc.class);
        job.setJobName("Word count");
        
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        
        job.setMapperClass(WordMapper.class);
        job.setReducerClass(CountReducer.class);
        
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        System.exit(job.waitForCompletion(true) ? 0 : 1);

    }//main class

    public static class WordMapper extends Mapper<Object,Text,Text,IntWritable>{
        //WordMapper class
        private final static IntWritable one =new IntWritable(1);
        private Text letter=new Text();

        @Override
        public void map(Object byteoffset,Text value,Context context) throws IOException,InterruptedException{
            String line=value.toString();
            
            //to convert all the letters to uppercase to make letter count case insensitive
            line=line.toUpperCase();
            
            //omit all characters other than A-Z
            line=line.replaceAll("[^A-Z]","");
            
            for (String tok : line.split("")) {
                                        
                    letter.set(tok);
                    context.write(letter,one);
                
            }//for loop
        }//map
    }//WordMapper

    public static class CountReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

        private IntWritable count=new IntWritable();
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context)
                throws IOException, InterruptedException {
            int count_letter = 0;

            for (IntWritable value : values) {
                count_letter += value.get();
            }
            count.set(count_letter);  
            context.write(key, this.count);
        }//reduce
    }//CountReducer
}//WordCount
