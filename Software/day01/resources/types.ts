export interface Robot {
	head?: {
		shape: string;
		color: string;
	};
	body?: {
		armor: string;
	};
	swimsuit?: {
		color: string;
	};
}

export type Callback = (err: Error | null, robot: Robot) => Robot | void;

export type Consumers = Array<(robot: Robot, cb: Callback) => Robot | void>;

export enum Country {
	FR = 'France',
	USA = 'United-State',
	RU = 'Russia',
	CHN = 'China',
	IND = 'India',
}

export enum Mission {
	ISS = 'ISS',
	MOON = 'MOON',
	MARS = 'MARS',
	EARTH = 'EARTH',
}

export enum Color {
	BLUE = 'blue',
	RED = 'red',
	GREEN = 'green',
	BLACK = 'black',
	YELLOW = 'yellow',
	PINK = 'pink',
	WHITE = 'white',
	PURPLE = 'purple',
}

export enum BodyKind {
	EMU = 'EMU',
	CES = 'CES',
	SOKOL = 'SOKOL',
	RO = 'RO',
}

export interface Cosmonaut {
	name: string;
	mission: Mission;
	country: Country;
}

export interface Suit {
	helmet?: {
		color: Color;
	};
	body?: {
		color: Color;
		kind: BodyKind;
	};
	gloves?: {
		color: Color;
	};
	boots?: {
		color: Color;
	};
}
