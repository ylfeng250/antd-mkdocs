## zh-CN

DatePicker 默认会根据 `picker` 的交互行为，自动选择是否需要确认按钮。你也可以通过 `needConfirm` 属性来手动设置是否需要确认按钮。当有 `needConfirm` 时，用户始终需要点击确认按钮才能完成选择。反之，则会在选择或者失去焦点时提交。

## en-US

DatePicker will automatically determine whether to show a confirm button according to the `picker` property. You can also set the `needConfirm` property to determine whether to show a confirm button. When `needConfirm` is set, the user must click the confirm button to complete the selection. Otherwise, the selection will be submitted when the picker loses focus or select a date.
```tsx
import React from 'react';
import type { DatePickerProps } from 'antd';
import { DatePicker, Space } from 'antd';
import type { Dayjs } from 'dayjs';

const onChange: DatePickerProps<Dayjs[]>['onChange'] = (date, dateString) => {
  console.log(date, dateString);
};

const App: React.FC = () => (
  <Space direction="vertical" size={12}>
    <DatePicker onChange={onChange} needConfirm />
    <DatePicker onChange={onChange} showTime needConfirm={false} />
  </Space>
);

export default App;
```
