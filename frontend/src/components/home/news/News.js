import React, { Component } from 'react';
import UpdateLog1_5 from './update-logs/UpdateLog1_5';
import UpdateLog1_6 from './update-logs/UpdateLog1_6';

export default class News extends Component {
	render() {
		return (
			<div>
				<br />
				<div className="title">News</div>
				<UpdateLog1_6 />
				<UpdateLog1_5 />
			</div>
		);
	}
}
