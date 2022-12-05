import React, { Component } from 'react';

export default class UpdateLog1_5 extends Component {
	render() {
		return (
			<div>
				<br />
				<u>CryptoApp 1.5 (2021-8-19)</u>
				<div>
					- Added ability to view live updates of coin and fund info on admin
					panel.
				</div>
				<div>
					- Changed communication method for coin and fund info with backend
					from http to websocket connection.
				</div>
			</div>
		);
	}
}
