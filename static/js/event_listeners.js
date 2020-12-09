// POPULATE DROPDOWN MENU WITH ALL STATES
const cases_link= '/usa_cases_today';
const deaths_link = '/usa_deaths_today';
const us_link = '/us_overall_today'
let colorFill;

// button state change:
var btnCases = $("#cases");
var btnDeaths = $("#deaths");


// $(document).ready(function(){
//     $("#myTab a").click(function(e){
//         e.preventDefault();
//         $(this).tab('show');
//     });
// });

// on load default params for cases button being active
let link = cases_link

d3.json(cases_link).then((Data)=>{
    let data = Data;
    let entries= Object.values(data);
    // console.log('entries '+ entries)
    // console.log(Object.values(entries))

    let i;
    statesList=[];
    datesList=[];
    statesList2=[];
    casesList=[];
    deathsList=[]
    abbrevsList=[];
    catList=[]

    for(i=0; i<entries.length; i++){
        let dataline=entries[i];
        
            let date_i =dataline[0].date;
            let state_i =dataline[0].state;
            let cases_i =dataline[0].cases;
            let abbrev_i=dataline[0].abbrev;
            let cat_i=dataline[0].category;
        
            datesList.push(date_i);
            statesList2.push(state_i);
            abbrevsList.push(abbrev_i);
            catList.push(cat_i);
            casesList.push(cases_i)
            
            let name= state_i
            // console.log(name)
            if (!(name in statesList)){
                statesList.push(name)
            };
    };
    // console.log('states list ' + statesList)
    
    //  Set the dropdown button with all subject IDs
    d3.select("#selDataset")
        .selectAll("option")
        .data(statesList.sort())
        .enter()
        .append("option")
        .html(function(d) {
            return d;
        })

    var colorScaling = d3.scaleThreshold()
        .domain([0, 1000, 5000, 10000, 50000, 100000, 500000, 1000000])
        .range(d3.schemeBlues[8]);
        
    // color the states on the map
    for (i=0; i<abbrevsList.length; i++){
        // console.log(catList[i])
        colorFill=colorScaling(casesList[i])
        d3.select('.'+ abbrevsList[i]).style("fill",colorFill)
        // console.log(("."+abbrevsList[i]))
        // console.log(casesList[i])
        d3.select('.'+ abbrevsList[i]).select('title').text(statesList2[i]+' Cases: '+ casesList[i])
    }
});

        
d3.select('#cases').on('click',  function(){
    // console.log('initializing cases function')
    d3.json(cases_link).then((Data)=>{
        let data = Data;
        let entries= Object.values(data);
        // console.log('entries '+ entries)
        // console.log(Object.values(entries))
    
        let i;
        statesList=[];
        datesList=[];
        statesList2=[];
        casesList=[];
        deathsList=[]
        abbrevsList=[];
        catList=[]
    
        for(i=0; i<entries.length; i++){
            let dataline=entries[i];
            
                let date_i =dataline[0].date;
                let state_i =dataline[0].state;
                let cases_i =dataline[0].cases;
                let abbrev_i=dataline[0].abbrev;
                let cat_i=dataline[0].category;
            
                datesList.push(date_i);
                statesList2.push(state_i);
                abbrevsList.push(abbrev_i);
                catList.push(cat_i);
                casesList.push(cases_i)
                
                let name= state_i
                // console.log(name)
                if (!(name in statesList)){
                    statesList.push(name)
                };
        };
        // console.log('states list ' + statesList.sort())
        
        //  Set the dropdown button with all subject IDs
        d3.select("#selDataset")
            .selectAll("option")
            .data(statesList.sort())
            .enter()
            .append("option")
            .html(function(d) {
                return d;
            })
    
        var colorScaling = d3.scaleThreshold()
            .domain([0, 1000, 5000, 10000, 50000, 100000, 500000, 1000000])
            .range(d3.schemeBlues[8]);
            
        // color the states on the map
        for (i=0; i<abbrevsList.length; i++){
            // console.log(catList[i])
            colorFill=colorScaling(casesList[i])
            d3.select('.'+ abbrevsList[i]).style("fill",colorFill)
            // console.log(("."+abbrevsList[i]))
            // console.log(casesList[i])
            d3.select('.'+ abbrevsList[i]).select('title').text(statesList2[i]+' Cases: '+ casesList[i])
        }
    });
});


d3.select('#deaths').on('click', function(){
    // console.log('initializing deaths function')
    d3.json(deaths_link).then((Data)=>{
        let data = Data;
        let entries= Object.values(data);
        // console.log('entries '+ entries)
        // console.log(Object.values(entries))
    
        let i;
        statesList=[];
        datesList=[];
        statesList2=[];
        deathsList=[]
        abbrevsList=[];
        catList=[]
    
        for(i=0; i<entries.length; i++){
            let dataline=entries[i];
            
                let date_i =dataline[0].date;
                let state_i =dataline[0].state;
                let deaths_i =dataline[0].deaths;
                let abbrev_i=dataline[0].abbrev;
                let cat_i=dataline[0].category;
            
                datesList.push(date_i);
                statesList2.push(state_i);
                abbrevsList.push(abbrev_i);
                catList.push(cat_i);
                deathsList.push(deaths_i)
                
                let name= state_i
                // console.log(name)
                if (!(name in statesList)){
                    statesList.push(name)
                };
        };
        // console.log('states list ' + statesList.sort())
        
        //  Set the dropdown button with all subject IDs
        d3.select("#selDataset")
            .selectAll("option")
            .data(statesList)
            .enter()
            .append("option")
            .html(function(d) {
                return d;
            })
    
        var colorScaling = d3.scaleThreshold()
            .domain([0, 50, 100, 500, 1000, 5000, 10000, 50000])
            .range(d3.schemeReds[8]);
            
        // color the states on the map
        for (i=0; i<abbrevsList.length; i++){
            // console.log(catList[i])
            colorFill=colorScaling(deathsList[i])
            d3.select('.'+ abbrevsList[i]).style("fill",colorFill)
            // console.log(("."+abbrevsList[i]))
            // console.log(deathsList[i])
            d3.select('.'+ abbrevsList[i]).select('title').text(statesList2[i]+' Deaths: '+ deathsList[i])
        }
    });
});

d3.json(us_link).then((Data)=>{
    let data = Data;
    // console.log(data)
    let entries= Object.values(data);
    // console.log(entries)
    let today_us_cases= Math.round(entries[0].cases);
    // console.log (today_us_cases)
    let today_us_deaths= Math.round(entries[0].deaths);
    // console.log(today_us_deaths)

    d3.select("#totalUSCases")
            .append("h5")
            .html(today_us_cases)

    d3.select("#totalUSDeaths")
            .append("h5")
            .html(today_us_deaths)
    
});

function init(){
    let state = 'Alabama'
    buildPlots(state)
};

init();

function optionChanged (){
    const dropDownMenu= d3.select('#selDataset');
    // console.log(dropDownMenu)
    let state = dropDownMenu.property('value') 
    buildPlots(state);
};

optionChanged();



function buildPlots(state){
    // define link for data from select state
    let cases_link= (`/${state}_cases`)
    let deaths_link= (`${state}_deaths`)
    let cases_forecast_link =(`/${state}_cases_forecast`)
    let deaths_forecast_link =(`/${state}_deaths_forecast`)
    // plot of cases over time

    d3.selectAll('#StateName')
        .html(state)

    d3.json(cases_link).then((Data)=>{
        let data3 = Data;
        let entries= Object.values(data3);
        // console.log('entries '+ entries)
        // console.log(Object.values(entries))
        state_today_cases=Math.round(entries[entries.length-1].cases);
        // console.log('state_today_cases:'+state_today_cases)
        state_today_date=Math.round(entries[entries.length-1].date);
        // console.log('state_today_date:'+state_today_date)

        d3.select("#totalStateCases")
            .text(state_today_cases)

        let i;
        statesList1=[];
        datesList1=[];
        statesList2=[];
        casesList1=[];

        for(i=0; i<entries.length; i++){
            let dataline=entries[i];
            // console.log(dataline)
            let date_i =dataline.date;
            let state_i =dataline.state;
            let cases_i =dataline.cases;

            datesList1.push(date_i);
            statesList2.push(state_i);
            casesList1.push(cases_i)
            // console.log(casesList1)
        };

        dailyCasesList=[]
        dailyDateList1=[]
        for (i=1; i<entries.length; i++){
            let dataline=entries[i];
            let yesterdataline=entries[i-1]
            let date_i =dataline.date;
            let cases_i =dataline.cases;
            let yester_cases_i=yesterdataline.cases
            let daily_cases_i= cases_i - yester_cases_i

            dailyCasesList.push(daily_cases_i);
            // console.log(dailyCasesList);
            dailyDateList1.push(date_i);

        };

        let x_cases= datesList1;
        let y_cases = casesList1;
        let x_daily_cases=dailyDateList1;
        let y_daily_cases= dailyCasesList;

        var Trace1= {
            x: x_cases,
            y: y_cases,
            mode: 'lines',
            name: (`Cases`),
            line: {
                dash: 'solid',
                width: 4,
                color:'blue'
            }
        };
        
        var Trace5={
            x:x_daily_cases,
            y:y_daily_cases,
            type: 'bar',
            yaxis: 'y',
            name:(`Daily Cases`),
            marker: {color: 'blue'}
        }

        d3.json(deaths_link).then((Data)=>{
            let data4 = Data;
            let entries= Object.values(data4);
            // console.log('entries '+ entries)
            // console.log(Object.values(entries))
            state_today_deaths=Math.round(entries[entries.length-1].deaths);
            // console.log('state_today_deaths:'+state_today_deaths)
            state_today_date=Math.round(entries[entries.length-1].date);
            // console.log('state_today_date:'+state_today_date)
    
            d3.select("#totalStateDeaths")
                .html(state_today_deaths)
    
            let i;
            statesList3=[];
            datesList2=[];
            deathsList2=[]
            for(i=0; i<entries.length; i++){
                let dataline=entries[i];
                let date_i =dataline.date;
                let deaths_i =dataline.deaths;
    
                datesList2.push(date_i);
                deathsList2.push(deaths_i);
            };

            dailyDeathsList=[]
            dailyDateList2=[]
            for (i=1; i<entries.length; i++){
                let dataline=entries[i];
                let yesterdataline=entries[i-1]
                let date_i =dataline.date;
                let deaths_i =dataline.deaths;
                let yester_deaths_i=yesterdataline.deaths
                let daily_deaths_i= deaths_i - yester_deaths_i

                dailyDeathsList.push(daily_deaths_i)
                dailyDateList2.push(date_i)
            };
       
            let x_deaths= datesList2
            let y_deaths = deathsList2
            let x_daily_deaths=dailyDateList2
            // console.log('x_daily_deaths:'+x_daily_deaths) 
            let y_daily_deaths= dailyDeathsList
            // console.log('y_daily_deaths:'+y_daily_deaths) 
            var Trace2= {
                x: x_deaths,
                y: y_deaths,
                yaxis: 'y2',
                mode: 'lines',
                name: (`Deaths`),
                line: {
                    dash: 'line',
                    width: 4,
                    color: 'red'
                }
            };

            var Trace6={
                x:x_daily_deaths,
                y:y_daily_deaths,
                type: 'bar',
                yaxis: 'y',
                name:(`Daily Deaths`),
                marker: {color: 'red'}
            };

            d3.json(cases_forecast_link).then((Data)=>{
                let data5 = Data;
                let entries= Object.values(data5);
                // console.log('entries '+ entries)
                // console.log(Object.values(entries))

                let i;
                let datesList3=[];
                let cases_list3=[];
                
                for(i=0; i<entries.length; i++){
                    let dataline=entries[i];
                    let date_i =dataline.date;
                    let cases_i =dataline.sarimax_cases_forecasted;
            
                    datesList3.push(date_i);
                    cases_list3.push(cases_i)
                };

                let x_cases_forecasted= datesList3
                let y_cases_forecasted = cases_list3

                var Trace3= {
                    x: x_cases_forecasted,
                    y: y_cases_forecasted,
                    yaxis: 'y',
                    mode: 'lines',
                    name: (`Forecasted Cases`),
                    line: {
                        dash: 'dot',
                        width: 4,
                        color: 'blue'
                    }
                };

                let dailyForecastedCasesList=[]
                let dailyForecastedDateList1=[]
                let j; 

                for (i=2; i<entries.length; i++){
                        let dataline=entries[i];
                        let yesterdataline=entries[i-1]
                        let date_i =dataline.date;
                        let cases_forecasted_i =dataline.sarimax_cases_forecasted;
                        // console.log('cases_forecasted_i:'+cases_forecasted_i)
                        let yester_cases_forecasted_i=yesterdataline.sarimax_cases_forecasted
                        // console.log('yester_cases_forecasted_i:'+yester_cases_forecasted_i)
                        
                        if (yester_cases_forecasted_i ===null){
                            daily_cases_forecasted_i= cases_forecasted_i- state_today_cases
                        }
                        else{
                            daily_cases_forecasted_i= cases_forecasted_i - yester_cases_forecasted_i
                        };

                        if(daily_cases_forecasted_i<0){
                            daily_cases_forecasted_i=0
                        };

                        dailyForecastedCasesList.push(daily_cases_forecasted_i);
                        dailyForecastedDateList1.push(date_i);
                
                };
        
                let x_daily_cases_forecasted=dailyForecastedDateList1;
                // console.log('x_daily_cases_forecasted'+x_daily_cases_forecasted)
                let y_daily_cases_forecasted= dailyForecastedCasesList;
                // console.log('y_daily_cases_forecasted'+y_daily_cases_forecasted)

                var Trace7= {
                    x: x_daily_cases_forecasted,
                    y: y_daily_cases_forecasted,
                    yaxis: 'y',
                    type: 'bar',
                    name:(`Daily Cases Forecasted`),
                    marker: {color: 'lightblue'}
                };

                d3.json(deaths_forecast_link).then((Data)=>{
                    let data6 = Data;
                    let entries= Object.values(data6);
                    // console.log('entries '+ entries)
                    // console.log(Object.values(entries))
    
                    let i;
                    let datesList4=[];
                    let deaths_list3=[]
                  
                    for(i=0; i<entries.length; i++){
                        let dataline=entries[i];
                        let date_i =dataline.date;
                        let deaths_i =dataline.sarimax_deaths_forecasted;
            
                        datesList4.push(date_i);
                        deaths_list3.push(deaths_i)
                    };

                    let x_deaths_forecasted= datesList4;
                    let y_deaths_forecasted = deaths_list3;

                    var Trace4= {
                        x: x_deaths_forecasted,
                        y: y_deaths_forecasted,
                        yaxis: 'y2',
                        mode: 'lines',
                        name: (`Forecasted Deaths`),
                        line: {
                            dash: 'dot',
                            width: 4,
                            color: 'red'
                        }
                    };

                    let dailyForecastedDeathsList=[]
                    let dailyForecastedDateList2=[]

                    for (i=1; i<entries.length; i++){
                        let dataline=entries[i];
                        let yesterdataline=entries[i-1]
                        let date_i =dataline.date;
                        let deaths_forecasted_i =dataline.sarimax_deaths_forecasted;
                        let yester_deaths_forecasted_i=yesterdataline.sarimax_deaths_forecasted
                        let daily_deaths_forecasted_i= deaths_forecasted_i - yester_deaths_forecasted_i
                        if (yester_deaths_forecasted_i ===null){
                            daily_deaths_forecasted_i= deaths_forecasted_i- state_today_deaths
                        }
                        else{
                            daily_deaths_forecasted_i= deaths_forecasted_i - yester_deaths_forecasted_i
                        };

                        if(daily_deaths_forecasted_i<0){
                            daily_deaths_forecasted_i=0
                        };

                        dailyForecastedDeathsList.push(daily_deaths_forecasted_i);
                        dailyForecastedDateList2.push(date_i);
                    };

                    let x_daily_deaths_forecasted=dailyForecastedDateList2;
                    // console.log('x_daily_deaths_forecasted:'+ x_daily_deaths_forecasted);
                    let y_daily_deaths_forecasted= dailyForecastedDeathsList;
                    // console.log('y_daily_deaths_forecasted:'+ y_daily_deaths_forecasted)

                    var Trace8= {
                        x: x_daily_deaths_forecasted,
                        y: y_daily_deaths_forecasted,
                        yaxis: 'y',
                        type: 'bar',
                        name:(`Daily Deaths Forecasted`),
                        marker: {color: 'pink'}
                    };

                    let data = [Trace1, Trace2, Trace3, Trace4];
                    let data2= [Trace5, Trace7];
                    // console.log('Trace5'+ Trace5);
                    // console.log('Trace7:'+Trace7);
                    let data3= [Trace6, Trace8];
                    // console.log('Trace6'+ Trace5)
                    // console.log('Trace8:'+Trace7)

                    var layout = {
                        autosize=false,
                        width: 1000,               
                        title: (`${state} Cumulative Covid-19 Cases & Deaths`),
                        xaxis: {
                            title: (`Date`),
                            autorange: true,
                            type: 'date'
                        },
                        yaxis: {
                            title:(`Cases`),
                            autorange: true,
                            titlefont: {color: 'blue'},
                            tickfont: {color: 'blue'},
                            showgrid:false
                        },
                        yaxis2: {
                            title: (`Deaths`),
                            titlefont: {color: 'red'},
                            tickfont: {color: 'red'},
                            overlaying: 'y',
                            side: 'right',
                            showgrid: false
                        },
                        legend: {
                            // y: 0.5,
                            // traceorder: 'reversed',
                            font: {
                            size: 16
                            },
                            // orientation: "h",
                            x:0.1,
                            y:1,
                            bgcolor: '#E2E2E2',
                            bordercolor: '#FFFFFF',
                            borderwidth: 2
                        }
                    };
                    var layout2 = {
                        autosize: false,
                        width: 1000,
                        title:(`${state} Daily Covid-19 Cases`),
                        xaxis: {
                            title: (`Date`),
                            autorange: true,
                            showgrid: true,
                            type: 'date'
                        },
                        yaxis: {
                            title:(`Daily Cases`),
                            autorange: true,
                            showgrid:false,
                            titlefont: {color: 'blue'},
                            tickfont: {color: 'blue'},
                        },
                        legend: {
                            font: {
                            size: 16
                            },
                            x:0.1,
                            y:1,
                            bgcolor: '#E2E2E2',
                            bordercolor: '#FFFFFF',
                            borderwidth: 2
                        }
                    };
                    var layout3={
                        autosize: false,
                        width: 1000,
                        title:(`${state} Daily Covid-19 Deaths`),
                        xaxis: {
                            title: (`Date`),
                            autorange: true,
                            type: 'date',
                            showgrid:true
                        },
                        yaxis: {
                            title: (`Daily Deaths`),
                            titlefont: {color: 'red'},
                            tickfont: {color: 'red'},
                            showgrid: false
                        },
                        legend: {
                            font: {
                            size: 16
                            },
                            x:0.1,
                            y:1,
                            bgcolor: '#E2E2E2',
                            bordercolor: '#FFFFFF',
                            borderwidth: 2
                        }
                    };

                    var config = {responsive: true};

                    Plotly.newPlot('plot', data, layout);
                    Plotly.newPlot('dailycaseplot', data2, layout2);
                    Plotly.newPlot('dailydeathplot', data3, layout3);
                });
            });
        });
    });
};