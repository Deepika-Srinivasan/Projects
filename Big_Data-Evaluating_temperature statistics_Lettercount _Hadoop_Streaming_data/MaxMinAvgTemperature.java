import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;
import org.apache.hadoop.io.Writable;
import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.mapreduce.lib.input.KeyValueTextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import java.io.DataInput;
import java.io.DataOutput;



public class MaxMinAvgTemperature {

  //NCDC Writable class
  public static class NCDCWritable implements Writable {
        public int max;
        public int min;
        public float avg;
        
        
        //default constructor for (de)serialization
        public NCDCWritable(int maxValue,int minValue,float avgValue) {
            max = maxValue;
            min = minValue;
            avg = avgValue;
        }
        
        @Override
        public void write(DataOutput dataOutput) throws IOException {
            dataOutput.writeInt(max); //write max temperature
            dataOutput.writeInt(min); //write min temperature
            dataOutput.writeFloat(avg); //write avg temperature
        }
        
        @Override
        public void readFields(DataInput dataInput) throws IOException {
            max=dataInput.readInt(); //read max temperature
            min=dataInput.readInt(); //read min temperature
            avg=dataInput.readFloat(); //reaad avg temperature
                       
        }
               
        @Override
        public String toString() {
            //maxvalue,minvalue and avgvalue
            return "Maximum = "+max+", Minimum = "+min+", Average = "+avg;
        }
    }
  
  //NCDC Writable class ends 

  public static void main(String[] args) throws Exception {
    if (args.length != 2) {
      System.err.println("Usage: MaxMinAvgTemperature <input path> <output path>");
      System.exit(-1);
    }
    
    Job job = new Job();
    job.setJarByClass(MaxMinAvgTemperature.class);
    job.setJobName("Max Min Avg temperature");

    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    
    job.setMapperClass(MaxMinAvgTemperatureMapper.class);
    job.setReducerClass(MaxMinAvgTemperatureReducer.class);
    
    job.setMapOutputKeyClass(Text.class);
    job.setMapOutputValueClass(IntWritable.class);

    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(NCDCWritable.class);//Reducer output value follows NCDC Writable
    
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }//main class
  
  public static class MaxMinAvgTemperatureMapper
  extends Mapper<LongWritable, Text, Text, IntWritable> {

  private static final int MISSING = 9999;
  
  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {
    
    String line = value.toString();
    String year = line.substring(15, 19);
    int airTemperature;
    if (line.charAt(87) == '+') { // parseInt doesn't like leading plus signs
      airTemperature = Integer.parseInt(line.substring(88, 92));
    } else {
      airTemperature = Integer.parseInt(line.substring(87, 92));
    }
    String quality = line.substring(92, 93);
    if (airTemperature != MISSING && quality.matches("[01459]")) {
      context.write(new Text(year), new IntWritable(airTemperature));
    }
  }
}//MaxMinAvgTemperatureMapper

public static class MaxMinAvgTemperatureReducer
  extends Reducer<Text, IntWritable, Text, NCDCWritable> {
  
  @Override
  public void reduce(Text key, Iterable<IntWritable> values,
      Context context)
      throws IOException, InterruptedException {
           
    int maxValue = Integer.MIN_VALUE;
    int minValue = Integer.MAX_VALUE;
    int temp_total_year=0;
    int count_values=0;
    float Average_temp_year;
        
    for (IntWritable value : values) {
      maxValue = Math.max(maxValue, value.get());
      minValue = Math.min(minValue, value.get());
      temp_total_year=temp_total_year+value.get();//add all temeperature for the key=year
      count_values=count_values+1;//count number of temperature values for the key=year
    }
    
    Average_temp_year=temp_total_year/count_values;
    
    //create new NCDCWritable object and assign values using the constructor created
    NCDCWritable ncdcWritable=new NCDCWritable(maxValue,minValue,Average_temp_year);
    
    //Reducer will write the output(year - max,min,avg) to HDFS
    context.write(key,ncdcWritable);
           	
  }//reduce
} //MaxMinAvgTemperatureReducer

}
//MaxMinAvgTemperature
