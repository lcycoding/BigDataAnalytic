A = LOAD '2008_hdfs.csv' USING PigStorage(',') AS (
    Year:chararray,
    Month:chararray,
    DayofMonth:chararray,
    DayOfWeek:chararray,
    DepTime:chararray,
    CRSDepTime:chararray,
    ArrTime:chararray,
    CRSArrTime:chararray,
    UniqueCarrier:chararray,
    FlightNum:chararray,
    TailNum:chararray,
    ActualElapsedTime:chararray,
    CRSElapsedTime:chararray,
    AirTime:chararray,
    ArrDelay:int,
    DepDelay:int,
    Origin:chararray,
    Dest:chararray,
    Distance:chararray,
    TaxiIn:chararray,
    TaxiOut:chararray,
    Cancelled:chararray,
    CancellationCode:chararray,
    Diverted:chararray,
    CarrierDelay:int,
    WeatherDelay:int,
    NASDelay:int,
    SecurityDelay:int,
    LateAircraftDelay:int);

B = FOREACH A GENERATE Year, Month, ArrDelay, DepDelay, Origin, Dest, CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,LateAircraftDelay;

C_G = GROUP B BY Month;
-- Q1
ANA = FOREACH C_G GENERATE 'Month:', group, AVG(B.ArrDelay) , MAX(B.ArrDelay);
ANAO = ORDER ANA BY $2 DESC;
DUMP ANAO;
-- Q2
WEA = FILTER B BY NOT WeatherDelay == 0;
WEA1 = GROUP WEA BY Year;

ANB = FOREACH WEA1 GENERATE group,'WeatherDelayCount' , COUNT(WEA.WeatherDelay),'WeatherDelayAverage', AVG(WEA.WeatherDelay);

ANBO = ORDER ANB BY $4 DESC;

DUMP ANBO; 
-- Q3
LOC = GROUP B BY Dest;
CAR = FOREACH LOC {
	cd = FILTER B BY NOT CarrierDelay == 0;
	wd = FILTER B BY NOT WeatherDelay == 0;
	nd = FILTER B BY NOT NASDelay == 0;
	sd = FILTER B BY NOT SecurityDelay == 0;
	lad = FILTER B BY NOT LateAircraftDelay == 0;
	GENERATE group ,'Delay ' , AVG(B.ArrDelay) ,'CarrierDelay ', COUNT(cd),'WeatherDelay ' ,COUNT(wd),'NASDelay ',COUNT(nd),'SecurityDelay ',COUNT(sd) , 'LateAircraftDelay ' ,COUNT(lad);
}

ANCO = ORDER CAR BY $2 DESC;

DUMP ANCO;
