import React, { Component } from 'react';

export default class UpdateLog1_6 extends Component {
	render() {
		return (
			<div>
				<br />
				<u>CryptopApp 1.6 (2021-8-21)</u>
				<div>- Added home page.</div>
				<div>- Added navigation options for admin and users on home page.</div>
				<div>- Added 'News' on home page</div>
				<div>
					- Changed all admin panel communication method with backend from http
					to websocket.
				</div>
				<div>- Changed ledger selection method on admin panel.</div>
			</div>
		);
	}
}
