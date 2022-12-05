import React from 'react';
import { useNavigate } from 'react-router-dom';
import News from './news/News';

export default function Home() {
	let navigate = useNavigate();

	const redirectAdmin = () => {
		navigate('/admin-panel');
	};

	return (
		<div>
			<br />
			<div className="title">Home</div>
			<button onClick={redirectAdmin}>Admin Login</button>
			<button>User Login</button>
			<News />
		</div>
	);
}

/*import React, { Component } from 'react';
import News from './news/News';

export default class Home extends Component {
	render() {
		return (
			<div>
				<br />
				<div className="title">Home</div>
				<button>Admin Login</button>
				<button>User Login</button>
				<News />
			</div>
		);
	}
}
*/
