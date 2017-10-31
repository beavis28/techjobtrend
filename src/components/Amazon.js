import React from 'react';
import _ from "lodash";
import {GridList, GridTile} from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';

const styles = {
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  gridList: {
    display: 'flex',
    flexWrap: 'nowrap',
    overflowX: 'auto',
  },
  titleStyle: {
    color: 'rgb(0, 188, 212)',
  },
};

class Amazon extends React.Component {
  state = {
    amazon_data : this.props.amazon_data
  }

  componentDidMount() {
  }
  componentDidUpdate(prevProps,prevState) {

  }

  render() {
    return (
      <div>
        <div className="App-title-desc">Most Relevant Books On High Demand Tech</div>

        <div style={styles.root}>
          <GridList style={styles.gridList} cols={2.2}>
            {this.props.amazon_data.map((tile) => (
              <GridTile
                key={tile.url}
                title={tile.title}
                titleStyle={styles.titleStyle}
                titleBackground="linear-gradient(to top, rgba(0,0,0,0.7) 0%,rgba(0,0,0,0.3) 70%,rgba(0,0,0,0) 100%)"
              >
                <img src={tile.media_url} />
              </GridTile>
            ))}
          </GridList>
        </div>
      </div>
    );
  }

  clickHandler = (value) => {
    window.open(value);
  }

}
export default Amazon;
