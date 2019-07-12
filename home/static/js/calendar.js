/* heavily influenced by Mark at https://codepen.io/xmark/pen/WQaXdv created November 08, 2015
*  Changes: no longer in <table> format, naming conventions, mobile support removed
*/


var Cal = function(divId) {

  //Store div id
  this.divId = divId;

  // Days of week, starting on Sunday
  this.DaysOfWeek = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
  ];

  // Months, stating on January
  this.Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ];

  // Set the current month, year
  var d = new Date();

  this.currMonth = d.getMonth();
  this.currYear = d.getFullYear();
  this.currDay = d.getDate();

};

// Goes to next month
Cal.prototype.nextMonth = function() {
  if ( this.currMonth == 11 ) {
    this.currMonth = 0;
    this.currYear = this.currYear + 1;
  }
  else {
    this.currMonth = this.currMonth + 1;
  }
  this.showcurr();
};

// Goes to previous month
Cal.prototype.previousMonth = function() {
  if ( this.currMonth == 0 ) {
    this.currMonth = 11;
    this.currYear = this.currYear - 1;
  }
  else {
    this.currMonth = this.currMonth - 1;
  }
  this.showcurr();
};

// Show current month
Cal.prototype.showcurr = function() {
  this.showMonth(this.currYear, this.currMonth);
};

// Show month (year, month)
Cal.prototype.showMonth = function(y, m) {

  var d = new Date()
  // First day of the week in the selected month
  , firstDayOfMonth = new Date(y, m, 1).getDay()
  // Last day of the selected month
  , lastDateOfMonth =  new Date(y, m+1, 0).getDate()
  // Last day of the previous month
  , lastDayOfLastMonth = m == 0 ? new Date(y-1, 11, 0).getDate() : new Date(y, m, 0).getDate();


  var html = '<div id="calendar">';

  // Write selected month and year
  html += '<header>';
  html += this.Months[m] + ' ' + y;
  html += '</header>';


  // Write the header of the days of the week
  html += '<ul class="day_names">';
  for(var i=0; i < this.DaysOfWeek.length;i++) {
    html += '<li>' + this.DaysOfWeek[i] + '</li>';
  }
  html += '</ul>';

  // Write the days
  var i=1;
  do {

    var dow = new Date(y, m, i).getDay();
    //for url format match
    mm=m;
    if(m<10){mm='0'+m};

    // If Sunday, start new row
    if ( dow == 0 ) {
      html += '<ul class="days">';
    }
    // If not Sunday but first day of the month
    // it will write the last days from the previous month
    else if ( i == 1 ) {
      html += '<ul class="days">';
      var k = lastDayOfLastMonth - firstDayOfMonth+1;
      yy=y;
      if(m<1){
        mm='12';
        yy=y-1;
      }
      for(var j=0; j < firstDayOfMonth; j++) {
        var url = dayList_url.replace(/0000/, yy).replace(/11/, mm).replace(/22/, k);
        html += '<a href= '+url+'>'+'<li class="other_month">' + '<div class="date">' + k + '</div></li></a>'
        k++;
      }
    }

    // Write the current day in the loop
    var chk = new Date();
    var chkY = chk.getFullYear();
    var chkM = chk.getMonth();
    if (chkY == this.currYear && chkM == this.currMonth && i == this.currDay) {
      mm=m+1;
      if(m+1<10){mm='0'+(m+1)};
      ii=i;
      if(i<10){ii='0'+i};
      var url = dayList_url.replace(/0000/, y).replace(/11/, mm).replace(/22/, ii);
      html += '<a href= '+url+'>'+'<li class="today">' + '<div class="date">' + i + '</div></li></a>'
    } else {
      mm=m+1;
      if(m+1<10){mm='0'+(m+1)};
      ii=i;
      if(i<10){ii='0'+i};
      var url = dayList_url.replace(/0000/, y).replace(/11/, mm).replace(/22/, ii);
      var datte = y + '-' + mm + '-' + ii;
      var res_count = '{% get_date_count reservation_list \'' + datte + '\' %}';
      // var res_count = day_counts.replace(/2018/, y).replace(/05/, mm).replace(/01/, ii);
      html += '<a href= '+url+'>'+'<li class="normal">' + '<div class="date">' + i + '</div></li></a>'
    }
    // If Saturday, closes the row
    if ( dow == 6 ) {
      html += '</ul>';
    }
    // If not Saturday, but last day of the selected month
    // it will write the next few days from the next month
    else if ( i == lastDateOfMonth ) {
      var k=1;
      mm=m+2;
      yy=y;
      if(m+2<10){mm='0'+(m+2)};
      if(m+2>12){
        mm='01';
        yy=y+1;
      }
      for(dow; dow < 6; dow++) {
        kk='0'+k;
        var url = dayList_url.replace(/0000/, yy).replace(/11/, mm).replace(/22/, kk);
        html += '<a href= '+url+'>'+'<li class="other_month">' + '<div class="date">' + k + '</div></li></a>';
        k++;
      }
    }

    i++;
  }while(i <= lastDateOfMonth);

  // Closes table
  html += '</div>';

  // Write HTML to the div
  document.getElementById(this.divId).innerHTML = html;
};

// On Load of the window
window.onload = function() {

  // Start calendar
  var c = new Cal("divCal");
  c.showcurr();

  // Bind next and previous button clicks
  getId('btnNext').onclick = function() {
    c.nextMonth();
  };
  getId('btnPrev').onclick = function() {
    c.previousMonth();
  };
}

// Get element by id
function getId(id) {
  return document.getElementById(id);
}