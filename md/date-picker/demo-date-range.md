## zh-CN

通过 `minDate` 和 `maxDate` 限定日期范围。

## en-US

Limit the range of dates by `minDate` and `maxDate`.
```tsx
import React from 'react';
import { DatePicker } from 'antd';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(customParseFormat);

const dateFormat = 'YYYY-MM-DD';

const App: React.FC = () => (
  <DatePicker
    defaultValue={dayjs('2019-09-03', dateFormat)}
    minDate={dayjs('2019-08-01', dateFormat)}
    maxDate={dayjs('2020-10-31', dateFormat)}
  />
);

export default App;
```
