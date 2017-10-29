import React from 'react';
import _ from "lodash";
import List, { ListItem, ListItemText } from 'material-ui/List';
import Avatar from 'material-ui/Avatar';

const style = {
  overflow: 'auto',
  maxHeight: 300,
  textAlign:"right"
};

class News extends React.Component {
  state = {
    rss_data : this.props.rss_data
  }

  render() {
    return (
      <div>
        <div className="App-title-desc">Latest Tech News</div>
        <List style={style} >
          {
            this.state.rss_data.map((v, index) =>
            <ListItem button>
              <Avatar alt={v.title} src={v.pic} /> 
              <ListItemText primary={v.title} secondary={v.published} onClick={() => this.clickHandler(v.link)}/>
            </ListItem> )
          }
        </List>
      </div>
    );
  }

  clickHandler = (value) => {
    window.open(value);
  }

}
export default News;
