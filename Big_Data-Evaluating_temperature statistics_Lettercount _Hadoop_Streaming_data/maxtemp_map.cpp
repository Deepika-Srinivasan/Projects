#include <string>
#include <iostream>
#include <regex>
#include <boost/algorithm/string.hpp>

int main()
{
	std::string line,year,temp,q;
	while(getline(std::cin,line)&& !line.empty())
		{
		//trim left and right spaces from the read input line
		boost::trim_right(line);
		boost::trim_left(line);
		
		//assign string values from read input line
		year=line.substr(15,4);
		temp=line.substr(87,5);
		q=line.substr(92,1);
		
		//check for missing temperature and quality matches 
		if(temp!="+9999" and std::regex_match(q,std::regex("[01459]")))
			{   
			 // Standard output year and temperature seperated by tab
				std::cout<<year<<"\t"<<temp<<std::endl;
			}
						
		}

}
