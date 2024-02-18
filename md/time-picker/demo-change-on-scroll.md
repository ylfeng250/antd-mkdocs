## zh-CN

通过 `changeOnScroll` 与 `needConfirm` 使其滚动时改变数值。

## en-US

Use `changeOnScroll` and `needConfirm` to change the value when scrolling.
```tsx
import React from 'react';
import { TimePicker } from 'antd';
import type { Dayjs } from 'dayjs';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(customParseFormat);

const onChange = (time: Dayjs, timeString: string) => {
  console.log(time, timeString);
};

const App: React.FC = () => <TimePicker onChange={onChange} changeOnScroll needConfirm={false} />;

export default App;
```
