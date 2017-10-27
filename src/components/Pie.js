/* global Plotly */
import React from 'react';
import _ from "lodash";

class Pie extends React.Component {
  componentDidMount() {
     if(_.isEmpty(this.props.data)){
       return;
     }
	   this.drawPie();
  }
  componentDidUpdate(prevProps,prevState) {
    if(_.isEmpty(this.props.data) && _.isEmpty(prevProps.data)){
      return;
    }
    this.drawPie();
  }

  render() {
    return (
      <div>
          <div className="Graph-title">% of all tags</div>
          <div id="pie"></div>
      </div>
    );
  }

  drawPie(){
    Plotly.newPlot('pie',this.props.data, {
      margin: {
        l: 50,
        r: 30,
        b: 30,
        t: 0,
        pad: 4
      }
    }, {
      displayModeBar: false
    });
  }

}
export default Pie;
