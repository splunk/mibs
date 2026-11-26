#
# PySNMP MIB module F5-ALERT-DEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-ALERT-DEF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:09:22 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
f5Compliance, platform = mibBuilder.importSymbols("F5-COMMON-SMI-MIB", "f5Compliance", "platform")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, Gauge32, Unsigned32, MibIdentifier, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Integer32, Counter32, Counter64, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Integer32", "Counter32", "Counter64", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
f5Alerts = ModuleIdentity((1, 3, 6, 1, 4, 1, 12276, 1, 1))
f5Alerts.setRevisions(('2019-08-01 09:41',))
if mibBuilder.loadTexts: f5Alerts.setLastUpdated('201908010941Z')
if mibBuilder.loadTexts: f5Alerts.setOrganization('F5 Networks, Inc.')
class F5Severity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("na", 8))

class F5CondEffect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 9999))
    namedValues = NamedValues(("clear", 0), ("assert", 1), ("event", 2), ("other", 9999))

f5AlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0))
f5AlertNotificationObject = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1))
f5AlertNotificationObjectGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2))
f5AlertNotificationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 3))
alertSource = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSource.setStatus('current')
alertEffect = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 2), F5CondEffect()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertEffect.setStatus('current')
alertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 3), F5Severity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertSeverity.setStatus('current')
alertTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertTimeStamp.setStatus('current')
alertDescription = MibScalar((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alertDescription.setStatus('current')
alertGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 12276, 1, 1, 0, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertSource"), ("F5-ALERT-DEF-MIB", "alertEffect"), ("F5-ALERT-DEF-MIB", "alertSeverity"), ("F5-ALERT-DEF-MIB", "alertTimeStamp"), ("F5-ALERT-DEF-MIB", "alertDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alertGroup = alertGroup.setStatus('current')
f5AlertGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 12276, 2, 1)).setObjects(("F5-ALERT-DEF-MIB", "alertGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f5AlertGroupCompliance = f5AlertGroupCompliance.setStatus('current')
mibBuilder.exportSymbols("F5-ALERT-DEF-MIB", alertDescription=alertDescription, alertGroup=alertGroup, f5AlertNotificationObject=f5AlertNotificationObject, f5AlertGroupCompliance=f5AlertGroupCompliance, f5AlertNotificationGroup=f5AlertNotificationGroup, F5CondEffect=F5CondEffect, alertSource=alertSource, F5Severity=F5Severity, f5AlertObjects=f5AlertObjects, PYSNMP_MODULE_ID=f5Alerts, alertTimeStamp=alertTimeStamp, f5AlertNotificationObjectGroup=f5AlertNotificationObjectGroup, alertEffect=alertEffect, alertSeverity=alertSeverity, f5Alerts=f5Alerts)
