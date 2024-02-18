## zh-CN

禁用时间选择。

## en-US

A disabled state of the `TimePicker`.
```tsx
import React from 'react';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { TimePicker } from 'antd';

dayjs.extend(customParseFormat);

const App: React.FC = () => <TimePicker defaultValue={dayjs('12:08:23', 'HH:mm:ss')} disabled />;

export default App;
```
