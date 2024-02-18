## zh-CN

输入格式对齐，通过键盘左右切换焦点。失去焦点时会尝试对齐到最后合法的日期。

## en-US

Align the date format. Switch the selection by arrow keys. Will try to align the date to the last valid date when blur.
```tsx
import React from 'react';
import type { DatePickerProps } from 'antd';
import { DatePicker, Space } from 'antd';

const onChange: DatePickerProps['onChange'] = (date, dateString) => {
  console.log(date, dateString);
};

const App: React.FC = () => (
  <Space direction="vertical">
    <DatePicker
      format={{
        format: 'YYYY-MM-DD',
        type: 'mask',
      }}
      onChange={onChange}
    />
    <DatePicker
      format={{
        format: 'YYYY-MM-DD HH:mm:ss',
        type: 'mask',
      }}
      onChange={onChange}
    />
  </Space>
);

export default App;
```
