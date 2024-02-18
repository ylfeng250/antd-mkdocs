---
category: Components
subtitle: 时间选择框
group: 数据录入
title: TimePicker
cover: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*kGmGSLk_1fwAAAAAAAAAAAAADrJ8AQ/original
coverDark: https://mdn.alipayobjects.com/huamei_7uahnr/afts/img/A*1hDmQJIDFJQAAAAAAAAAAAAADrJ8AQ/original
demo:
  cols: 2
---

输入或选择时间的控件。

## 何时使用

当用户需要输入一个时间，可以点击标准输入框，弹出时间面板进行选择。

## 代码演示

<!-- prettier-ignore -->
<code src="./demo/basic.tsx">基本</code>
<code src="./demo/value.tsx">受控组件</code>
<code src="./demo/size.tsx">三种大小</code>
<code src="./demo/disabled.tsx">禁用</code>
<code src="./demo/hide-column.tsx">选择时分</code>
<code src="./demo/interval-options.tsx">步长选项</code>
<code src="./demo/addon.tsx">附加内容</code>
<code src="./demo/12hours.tsx">12 小时制</code>
<code src="./demo/change-on-scroll.tsx" version="5.14.0">滚动即改变</code>
<code src="./demo/colored-popup.tsx" debug>色付きポップアップ</code>
<code src="./demo/range-picker.tsx">范围选择器</code>
<code src="./demo/variant.tsx" version="5.13.0">多种形态</code>
<code src="./demo/status.tsx">自定义状态</code>
<code src="./demo/suffix.tsx" debug>后缀图标</code>
<code src="./demo/render-panel.tsx" debug>_InternalPanelDoNotUseOrYouWillBeFired</code>

## API

---

通用属性参考：[通用属性](/docs/react/common-props)

```jsx
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat'

dayjs.extend(customParseFormat)
<TimePicker defaultValue={dayjs('13:30:56', 'HH:mm:ss')} />;
```

| 参数 | 说明 | 类型 | 默认值 | 版本 |
| --- | --- | --- | --- | --- |
| allowClear | 自定义清除按钮 | boolean \| { clearIcon?: ReactNode } | true | 5.8.0: 支持对象类型 |
| autoFocus | 自动获取焦点 | boolean | false |  |
| cellRender | 自定义单元格的内容 | (current: number, info: { originNode: React.ReactNode, today: dayjs, range?: 'start' \| 'end', subType: 'hour' \| 'minute' \| 'second' \| 'meridiem' }) => React.ReactNode | - | 5.4.0 |
| changeOnScroll | 在滚动时改变选择值 | boolean | false | 5.14.0 |
| className | 选择器类名 | string | - |  |
| defaultValue | 默认时间 | [dayjs](http://day.js.org/) | - |  |
| disabled | 禁用全部操作 | boolean | false |  |
| disabledTime | 不可选择的时间 | [DisabledTime](#disabledtime) | - | 4.19.0 |
| format | 展示的时间格式 | string | `HH:mm:ss` |  |
| getPopupContainer | 定义浮层的容器，默认为 body 上新建 div | function(trigger) | - |  |
| hideDisabledOptions | 隐藏禁止选择的选项 | boolean | false |  |
| hourStep | 小时选项间隔 | number | 1 |  |
| inputReadOnly | 设置输入框为只读（避免在移动设备上打开虚拟键盘） | boolean | false |  |
| minuteStep | 分钟选项间隔 | number | 1 |  |
| needConfirm | 是否需要确认按钮，为 `false` 时失去焦点即代表选择 | boolean | - | 5.14.0 |
| open | 面板是否打开 | boolean | false |  |
| placeholder | 没有值的时候显示的内容 | string \| \[string, string] | `请选择时间` |  |
| placement | 选择框弹出的位置 | `bottomLeft` `bottomRight` `topLeft` `topRight` | bottomLeft |  |
| popupClassName | 弹出层类名 | string | - |  |
| popupStyle | 弹出层样式对象 | object | - |  |
| renderExtraFooter | 选择框底部显示自定义的内容 | () => ReactNode | - |  |
| secondStep | 秒选项间隔 | number | 1 |  |
| showNow | 面板是否显示“此刻”按钮 | boolean | - | 4.4.0 |
| size | 输入框大小，`large` 高度为 40px，`small` 为 24px，默认是 32px | `large` \| `middle` \| `small` | - |  |
| status | 设置校验状态 | 'error' \| 'warning' | - | 4.19.0 |
| suffixIcon | 自定义的选择框后缀图标 | ReactNode | - |  |
| use12Hours | 使用 12 小时制，为 true 时 `format` 默认为 `h:mm:ss a` | boolean | false |  |
| value | 当前时间 | [dayjs](http://day.js.org/) | - |  |
| variant | 形态变体 | `outlined` \| `borderless` \| `filled` | `outlined` | 5.13.0 |
| onChange | 时间发生变化的回调 | function(time: dayjs, timeString: string): void | - |  |
| onOpenChange | 面板打开/关闭时的回调 | (open: boolean) => void | - |  |

#### DisabledTime

```typescript
type DisabledTime = (now: Dayjs) => {
  disabledHours?: () => number[];
  disabledMinutes?: (selectedHour: number) => number[];
  disabledSeconds?: (selectedHour: number, selectedMinute: number) => number[];
  disabledMilliseconds?: (
    selectedHour: number,
    selectedMinute: number,
    selectedSecond: number,
  ) => number[];
};
```

注意：`disabledMilliseconds` 为 `5.14.0` 新增。

## 方法

| 名称    | 描述     | 版本 |
| ------- | -------- | ---- |
| blur()  | 移除焦点 |      |
| focus() | 获取焦点 |      |

## RangePicker

属性与 DatePicker 的 [RangePicker](/components/date-picker-cn#rangepicker) 相同。还包含以下属性：

| 参数         | 说明                 | 类型                                    | 默认值 | 版本   |
| ------------ | -------------------- | --------------------------------------- | ------ | ------ |
| disabledTime | 不可选择的时间       | [RangeDisabledTime](#rangedisabledtime) | -      | 4.19.0 |
| order        | 始末时间是否自动排序 | boolean                                 | true   | 4.1.0  |

### RangeDisabledTime

```typescript
type RangeDisabledTime = (
  now: Dayjs,
  type = 'start' | 'end',
) => {
  disabledHours?: () => number[];
  disabledMinutes?: (selectedHour: number) => number[];
  disabledSeconds?: (selectedHour: number, selectedMinute: number) => number[];
};
```

## 主题变量（Design Token）

<ComponentTokenTable component="DatePicker"></ComponentTokenTable>

## FAQ

- [如何在 TimePicker 中使用自定义日期库（如 Moment.js ）](/docs/react/use-custom-date-library#timepicker)

## size demo
>/demo/size.tsx


三种大小的输入框，大的用在表单中，中的为默认。



The input box comes in three sizes. large is used in the form, while the medium size is the default.
```tsx
import React from 'react';
import dayjs from 'dayjs';
import { Space, TimePicker } from 'antd';

const App: React.FC = () => (
  <Space wrap>
    <TimePicker defaultValue={dayjs('12:08:23', 'HH:mm:ss')} size="large" />
    <TimePicker defaultValue={dayjs('12:08:23', 'HH:mm:ss')} />
    <TimePicker defaultValue={dayjs('12:08:23', 'HH:mm:ss')} size="small" />
  </Space>
);

export default App;
```

## colored-popup demo
>/demo/colored-popup.tsx


将自定义 class 传给 `TimePicker` 弹框。



Passing custom class to `TimePicker` popup.
```tsx
import React from 'react';
import type { Dayjs } from 'dayjs';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { TimePicker } from 'antd';

dayjs.extend(customParseFormat);

const onChange = (time: Dayjs, timeString: string) => {
  console.log(time, timeString);
};

const App: React.FC = () => (
  <TimePicker
    onChange={onChange}
    defaultOpenValue={dayjs('00:00:00', 'HH:mm:ss')}
    popupClassName="myCustomClassName"
  />
);

export default App;
```

## change-on-scroll demo
>/demo/change-on-scroll.tsx


通过 `changeOnScroll` 与 `needConfirm` 使其滚动时改变数值。



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

## hide-column demo
>/demo/hide-column.tsx


TimePicker 浮层中的列会随着 `format` 变化，当略去 `format` 中的某部分时，浮层中对应的列也会消失。



While part of `format` is omitted, the corresponding column in panel will disappear, too.
```tsx
import React from 'react';
import dayjs from 'dayjs';
import { TimePicker } from 'antd';

const format = 'HH:mm';

const App: React.FC = () => <TimePicker defaultValue={dayjs('12:08', format)} format={format} />;

export default App;
```

## 12hours demo
>/demo/12hours.tsx


12 小时制的时间选择器，默认的 format 为 `h:mm:ss a`。



TimePicker of 12 hours format, with default format `h:mm:ss a`.
```tsx
import React from 'react';
import type { Dayjs } from 'dayjs';
import { Space, TimePicker } from 'antd';

const onChange = (time: Dayjs, timeString: string) => {
  console.log(time, timeString);
};

const App: React.FC = () => (
  <Space wrap>
    <TimePicker use12Hours onChange={onChange} />
    <TimePicker use12Hours format="h:mm:ss A" onChange={onChange} />
    <TimePicker use12Hours format="h:mm a" onChange={onChange} />
  </Space>
);

export default App;
```

## addon demo
>/demo/addon.tsx


在 TimePicker 选择框底部显示自定义的内容。



Render addon contents to time picker panel's bottom.
```tsx
import React, { useState } from 'react';
import { Button, TimePicker } from 'antd';

const App: React.FC = () => {
  const [open, setOpen] = useState(false);

  return (
    <TimePicker
      open={open}
      onOpenChange={setOpen}
      renderExtraFooter={() => (
        <Button size="small" type="primary" onClick={() => setOpen(false)}>
          OK
        </Button>
      )}
    />
  );
};

export default App;
```

## value demo
>/demo/value.tsx


value 和 onChange 需要配合使用。



`value` and `onChange` should be used together,
```tsx
import React, { useState } from 'react';
import type { Dayjs } from 'dayjs';
import { TimePicker } from 'antd';

const App: React.FC = () => {
  const [value, setValue] = useState<Dayjs | null>(null);

  const onChange = (time: Dayjs) => {
    setValue(time);
  };

  return <TimePicker value={value} onChange={onChange} />;
};

export default App;
```

## variant demo
>/demo/variant.tsx


无边框样式。



Bordered-less style component.
```tsx
import React from 'react';
import { Flex, TimePicker } from 'antd';

const { RangePicker } = TimePicker;

const App: React.FC = () => (
  <Flex vertical gap={12}>
    <Flex gap={8}>
      <TimePicker placeholder="Filled" />
      <RangePicker placeholder={['Filled', '']} />
    </Flex>
    <Flex gap={8}>
      <TimePicker variant="filled" placeholder="Filled" />
      <RangePicker variant="filled" placeholder={['Filled', '']} />
    </Flex>
    <Flex gap={8}>
      <TimePicker variant="borderless" placeholder="Borderless" />
      <RangePicker variant="borderless" placeholder={['Borderless', '']} />
    </Flex>
  </Flex>
);

export default App;
```

## interval-options demo
>/demo/interval-options.tsx


可以使用 `hourStep` `minuteStep` `secondStep` 按步长展示可选的时分秒。



Show stepped options by `hourStep` `minuteStep` `secondStep`.
```tsx
import React from 'react';
import { TimePicker } from 'antd';

const App: React.FC = () => <TimePicker minuteStep={15} secondStep={10} hourStep={1} />;

export default App;
```

## render-panel demo
>/demo/render-panel.tsx


调试用组件，请勿直接使用。



Debug usage. Do not use in your production.
```tsx
import React from 'react';
import { TimePicker } from 'antd';

const { _InternalPanelDoNotUseOrYouWillBeFired: InternalTimePicker } = TimePicker;

const App: React.FC = () => <InternalTimePicker />;

export default App;
```

## disabled demo
>/demo/disabled.tsx


禁用时间选择。



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

## status demo
>/demo/status.tsx


使用 `status` 为 TimePicker 添加状态，可选 `error` 或者 `warning`。



Add status to TimePicker with `status`, which could be `error` or `warning`.
```tsx
import React from 'react';
import { Space, TimePicker } from 'antd';

const App: React.FC = () => (
  <Space direction="vertical">
    <TimePicker status="error" />
    <TimePicker status="warning" />
    <TimePicker.RangePicker status="error" />
    <TimePicker.RangePicker status="warning" />
  </Space>
);

export default App;
```

## suffix demo
>/demo/suffix.tsx


点击 TimePicker，然后可以在浮层中选择或者输入某一时间。



Click `TimePicker`, and then we could select or input a time in panel.
```tsx
import React from 'react';
import { SmileOutlined } from '@ant-design/icons';
import type { Dayjs } from 'dayjs';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { TimePicker } from 'antd';

dayjs.extend(customParseFormat);

const onChange = (time: Dayjs, timeString: string) => {
  console.log(time, timeString);
};

const App: React.FC = () => (
  <TimePicker
    suffixIcon={<SmileOutlined />}
    onChange={onChange}
    defaultOpenValue={dayjs('00:00:00', 'HH:mm:ss')}
  />
);

export default App;
```

## basic demo
>/demo/basic.tsx


点击 TimePicker，然后可以在浮层中选择或者输入某一时间。



Click `TimePicker`, and then we could select or input a time in panel.
```tsx
import React from 'react';
import type { Dayjs } from 'dayjs';
import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { TimePicker } from 'antd';

dayjs.extend(customParseFormat);

const onChange = (time: Dayjs, timeString: string) => {
  console.log(time, timeString);
};

const App: React.FC = () => (
  <TimePicker onChange={onChange} defaultOpenValue={dayjs('00:00:00', 'HH:mm:ss')} />
);

export default App;
```

## range-picker demo
>/demo/range-picker.tsx


通过 `TimePicker.RangePicker` 使用时间范围选择器。



Use time range picker with `TimePicker.RangePicker`.
```tsx
import React from 'react';
import { TimePicker } from 'antd';

const App: React.FC = () => <TimePicker.RangePicker />;

export default App;
```
