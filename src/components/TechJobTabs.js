/* eslint-disable flowtype/require-valid-file-annotation */
/* eslint-disable react/no-multi-comp */

import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Tabs, { Tab } from 'material-ui/Tabs';
import RankingsTable from './RankingsTable';
import News from './News';
import Amazon from './Amazon';

function TabContainer(props) {
  return <div style={{ padding: 8 * 3 }}>{props.children}</div>;
}

TabContainer.propTypes = {
  children: PropTypes.node.isRequired,
};

const styles = theme => ({
  root: {
    flexGrow: 1,
    marginTop: theme.spacing.unit * 0,
    backgroundColor: theme.palette.background.paper,
  },
});

class TechJobTabs extends React.Component {
  state = {
    value: 0,
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;

    return (
      <div className={classes.root}>
          <Tabs value={value} onChange={this.handleChange} centered indicatorColor="primary">
            <Tab label="Total Rank" href="#total-rank"/>
            <Tab label="Tech News" href="#news" />
            <Tab label="Tech Book Rank" href="#ebook-rank" />
          </Tabs>
        {value === 0 && <TabContainer>            
            <RankingsTable
                tags={this.props.tags}
                history={this.props.history}
                location={this.props.location}/></TabContainer>}
        {value === 1 && <TabContainer>
            <News rss_data={this.props.rss_data} />
            </TabContainer>}
        {value === 2 && <TabContainer>
            <Amazon amazon_data={this.props.amazon_data}/>
            </TabContainer>}
      </div>
    );
  }
}

TechJobTabs.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(TechJobTabs);