import React from 'react';

import qs from 'qs';
import _ from 'lodash';
import Button from 'material-ui/Button';
import Table, { TableBody, TableCell, TableHead, TableRow } from 'material-ui/Table';
import Grid from 'material-ui/Grid';
import News from './News';
import Amazon from './Amazon';

import changesData from '../data/top_changes.json';

const style = {
  margin: 12,
};

class ThreeGrid  extends React.Component {

 componentWillMount() {
 }

  render(){
    return (
      <div className="changes">
        <div className="changes-tables-container">
              <Grid container spacing={24}>
                 <Grid item xs={6}>
                 <News rss_data={this.props.rss_data} />
                </Grid>
                <Grid item xs={6}>
                 <Amazon amazon_data={this.props.amazon_data}/>
                </Grid>
            </Grid>
        </div>
      </div>
    )
  }

}

export default ThreeGrid;