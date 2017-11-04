import React from 'react';

import qs from 'qs';
import _ from 'lodash';
import Button from 'material-ui/Button';
import Table, { TableBody, TableCell, TableHead, TableRow } from 'material-ui/Table';
import Grid from 'material-ui/Grid';
import Select from 'material-ui/Select';
import { MenuItem } from 'material-ui/Menu';

import country_data from '../data/country_data.json';

const style = {
  margin: 12,
};

class CountryRanking  extends React.Component {
   state = {
    btnSelection: "CA",
  };

 componentWillMount() {
 }

  render(){
    return (
      <div className="changes">
        <div className="buttons-container">
          <div>
            Country/State Tech Rank
          </div>
          <div>
            <Select value={this.state.btnSelection} onChange={this.clickHandler('btnSelection')} >
            {
                country_data.map((v, index) => <MenuItem key={index} value={Object.keys(v)[0]}>{Object.keys(v)[0]}</MenuItem> )
            }
            </Select>
          </div>
        </div>
        <div className="changes-tables-container">
              <Grid container spacing={24}>
                 <Grid item xs={12}>
                    <Table >
                      {this.renderTableHeader()}
                     <TableBody>
                        {this.renderRows("San Francisco, CA")}
                        </TableBody>
                    </Table>
                </Grid>
            </Grid>
        </div>
      </div>
    )
  }

  renderTableHeader(){
    return (
      <TableHead >
        <TableRow>
          <TableCell className="table-column">Rank</TableCell>  
          <TableCell className="table-column">Tech</TableCell>
          <TableCell className="table-column">Posted Job Count</TableCell>  
        </TableRow>
      </TableHead>
    )
  }

  renderRows(type){
    let rows;
    for (var i = 0; i < country_data.length; i++) {
        var obj = country_data[i];
        if (Object.keys(obj) == this.state.btnSelection) {
            let value = Object.values(obj);
            rows = value[0].map((v, index)=>
              <TableRow onClick={(event)=>this.rowSelected(index,type)} key={"row-"+v[0]} className="table-row table-pointer">
                <TableCell key={"cell-rank-"+(index+1)} className="table-column table-pointer">{index+1}</TableCell>
                <TableCell key={"cell-tag-"+v[0]} className="table-column table-pointer">{v[0]}</TableCell>
                <TableCell key={"cell-change-"+index} className="table-column table-pointer"> {v[1]} </TableCell>
              </TableRow>
            );
            break;
        }
    }

    return rows;
  }

  rowSelected(index,type){
    if(!_.isUndefined(index)){
        let tag ='';
        for (var i = 0; i < country_data.length; i++) {
            var obj = country_data[i];
            if (Object.keys(obj) == this.state.btnSelection) {
                let value = Object.values(obj);
                this.applyQuery(value[0][index][0]);
                break;
            }
        }
    }
  };

  clickHandler = (value) => event => {
    this.setState({
      btnSelection: event.target.value
    });
  };

  applyQuery = (selection) =>{
    let oldQuery = this.props.location.search;
    oldQuery = qs.parse(oldQuery.substring(1));
    let payload = [selection]
    if(!_.isEmpty(oldQuery.keywords)){
      payload = _.union([payload,oldQuery.keywords]);
    }
    let newQueryPayload = { "keywords": payload.join() };
    this.props.history.push("?"+qs.stringify(newQueryPayload,{ encode: true }));
    this.setState({value: ""});
  }

}

export default CountryRanking;
