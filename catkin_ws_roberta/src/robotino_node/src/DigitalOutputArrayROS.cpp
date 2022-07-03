/*
 * DigitalOutputArrayROS.cpp
 *
 *  Created on: 09.12.2011
 *      Author: indorewala@servicerobotics.eu
 */

#include "DigitalOutputArrayROS.h"

DigitalOutputArrayROS::DigitalOutputArrayROS()
{
	digital_sub_ = nh_.subscribe("set_digital_values", 1,
			&DigitalOutputArrayROS::setDigitalValuesCallback, this);
}

DigitalOutputArrayROS::~DigitalOutputArrayROS()
{
	digital_sub_.shutdown();
}

void DigitalOutputArrayROS::setDigitalValuesCallback( const robotino_msgs::DigitalReadingsConstPtr& msg)
{
	int numValues = msg->values.size();
	if( numValues > 0 )
	{
		bool values[numValues];

		memcpy( values, msg->values.data(), numValues * sizeof(bool) );
		
		
		int val[numValues];
		for(int i = 0; i< numValues; i++) {
			if(values[i]){
				val[i] = 1;
			}
		}
		
		setValues( val, numValues );
	}
}
