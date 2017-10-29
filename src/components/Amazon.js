import React from 'react';
import _ from "lodash";

const style = {
  overflow: 'auto',
  maxHeight: 300,
  textAlign:"right"
};

class Amazon extends React.Component {
  state = {
    rss_data : this.props.rss_data
  }

  componentDidMount() {
  }
  componentDidUpdate(prevProps,prevState) {

  }

  render() {
    return (
      <div>
        <div className="App-title-desc">Recommended Tech Book</div>
        </div>
    );
  }

  clickHandler = (value) => {
    window.open(value);
  }

}
export default Amazon;
