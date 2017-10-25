import React from 'react';

import qs from 'qs';
import _ from 'lodash';
import Paper from 'material-ui/Paper';
import Grid from 'material-ui/Grid';

const style = {
    flex:1,
    margin: 20,
    textAlign: 'center',
    display: 'inline-block',
}

class News extends React.Component {
   state = {
    btnSelection: "top25",
  };

 componentWillMount() {
 }

  render(){
    return (
      <div className="news">
        <Grid container spacing={24}  >
          <Paper style={style} zDepth={3}>
          test
          </Paper>
        </Grid>
      </div>
    )
  }
}

export default News;