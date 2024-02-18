## zh-CN

可以使用 `hourStep` `minuteStep` `secondStep` 按步长展示可选的时分秒。

## en-US

Show stepped options by `hourStep` `minuteStep` `secondStep`.
```tsx
import React from 'react';
import { TimePicker } from 'antd';

const App: React.FC = () => <TimePicker minuteStep={15} secondStep={10} hourStep={1} />;

export default App;
```
