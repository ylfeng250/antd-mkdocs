## zh-CN

在范围选择时，可以允许留空。这对于需要保留“至今”日期项颇为有用。

## en-US

Allow empty for the RangePicker. It's useful when you need to keep the "to date".
```tsx
import React from 'react';
import { DatePicker } from 'antd';

const App: React.FC = () => (
  <DatePicker.RangePicker
    placeholder={['', 'Till Now']}
    allowEmpty={[false, true]}
    onChange={(date, dateString) => {
      console.log(date, dateString);
    }}
  />
);

export default App;
```
