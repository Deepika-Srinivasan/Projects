#include <iostream> 
#include <string>
#include <algorithm>
#include <climits> //to use INT_MIN values

int main()
{
	std::string mapperoutput;
	std::string last_key="";
	int max_val=INT_MIN;

  	while (std::getline(std::cin, mapperoutput))
  	{
    	std::string reducerinput=mapperoutput;
    	std::string delimiter = "\t";
    	
    	//find the delimeter position and store in tabposition
    	int tabposition=reducerinput.find(delimiter);
    	
    	//extract the key from position 0 for tabposition number of characters.This will give the year 
    	std::string year = reducerinput.substr(0,tabposition);
    	
    	//Extract the temperature that is just after the tab
    	std::string temp=  reducerinput.substr(tabposition+1);
    	
    	    	
       	if(last_key!="" && last_key != year)
    	{   
    		//Once the year changed print the previous year and the max temperature found for that year
      		std::cout << last_key<<"\t"<< max_val<< std::endl;
      		
      		//Next Unique year
      		last_key=year;
      		max_val=std::stoi(temp);
    	} 
    	
    	else
    	{   
    		//find the max temperature for a particular year 
        	last_key= year;
        	
        	//compare with previous max temperatures found earlier and find the overall max temperature for the year 
        	max_val=std::max(max_val, std::stoi(temp));
    	}
    
  	}//end of while loop
  
    //Last year and max temperature will be missed in the while loop.
 	if(last_key!=""){
   	std::cout << last_key<<"\t"<< max_val<< std::endl;
 }

}


