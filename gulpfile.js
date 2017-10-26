const gulp = require('gulp');
const shell = require('gulp-shell');

gulp.task('scrape', shell.task([
  'cd jobScrape && python main.py'
]));

gulp.task('move_data', [], () => {
  return gulp.src('jobScrape/*.json')
    .pipe(gulp.dest('./dataProcess/new'))
});

gulp.task('process', ['move_data'], shell.task([
  'cd dataProcess && python process_tag_data.py && python reconcile_tag_data.py && python make_pie_data.py && python region_data.py'
]));

gulp.task('data', ['move_data', 'process'], () => {
  return gulp.src('dataProcess/result/*.json')
    .pipe(gulp.dest('./src/data'))
});
