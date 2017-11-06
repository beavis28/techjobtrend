import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import Card, { CardActions, CardContent } from 'material-ui/Card';
import Button from 'material-ui/Button';
import Typography from 'material-ui/Typography';
import { blue, lightBlue } from 'material-ui/colors';

const primary = blue[500]; // #F44336

const styles = theme => ({
  card: {
    margin: 50,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    marginBottom: 16,
    fontSize: 22,
    color: primary,
  },
  pos: {
    marginBottom: 12,
    color: theme.palette.text.secondary,
  },
});

function Opinion(props) {
  const { classes } = props;

  return (
    <div>
      <Card className={classes.card}>
        <CardContent>
          <Typography type="headline" className={classes.title} >
            Java and Javascript still domain job markets
          </Typography>
          <Typography type="body1" className={classes.pos}>
            - Report on November first week -
          </Typography>
          <Typography component="p">
            so this week, finally machine learning got first 50 at first time. At the same time, we can see all of ML related tech is rising.<br />
            so this week, finally machine learning got first 50 at first time. At the same time, we can see all of ML related tech is rising.<br />
          </Typography>
        </CardContent>
        <CardActions>
          <Button dense>Learn More</Button>
        </CardActions>
      </Card>
    </div>
  );
}

Opinion.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Opinion);
