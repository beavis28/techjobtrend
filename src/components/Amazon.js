import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import { GridList, GridListTile, GridListTileBar } from 'material-ui/GridList';
import IconButton from 'material-ui/IconButton';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';

const styles = theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    background: theme.palette.background.paper,
  },
  img : {
    width: 112,
    height: 160,
    margin: "auto",
    display: "block",
  },
  gridList: {
    flexWrap: 'wrap',
    // Promote the list into his own layer on Chrome. This cost memory but helps keeping high FPS.
    transform: 'translateZ(0)',
    margin:'50px',
    cursor:"pointer",
  },
  title: {
    fontSize: '90%',
    //whiteSpace: 'normal',
  },
  titleBar: {
    // background:
    //   'linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
    //height: 90,
  },
});

function Amazon(props) {
  const { classes } = props;

  function clickHandler (value) {
    window.open(value);
  }

  return (
    <div className={classes.root}>
      <AppBar position="static" >
        <Toolbar>
          <Typography type="title" color="inherit">
            High Demand Tech Books
          </Typography>
        </Toolbar>
      </AppBar>
      <GridList className={classes.gridList} cols={2} >
        {props.amazon_data.map(tile => (
          <GridListTile key={tile.url} onClick={() => clickHandler(tile.url)}>
            <img src={tile.image} alt={tile.title} className={classes.img}/>
            <GridListTileBar
              title={tile.title}
              classes={{
                root: classes.titleBar,
                title: classes.title,
              }}
            />
            
          </GridListTile>
        ))}
      </GridList>
    </div>
  );
}

Amazon.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Amazon);
