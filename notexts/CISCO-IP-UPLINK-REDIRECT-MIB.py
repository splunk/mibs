#
# PySNMP MIB module CISCO-IP-UPLINK-REDIRECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-UPLINK-REDIRECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoIpUplinkRedirectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 191))
ciscoIpUplinkRedirectMIB.setRevisions(('2001-01-22 00:00',))
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setLastUpdated('200101220000Z')
if mibBuilder.loadTexts: ciscoIpUplinkRedirectMIB.setOrganization('Cisco Systems, Inc.')
ciscoIpUplinkRedirectMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 1))
ciurStartupStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ciurStartupStatus.setStatus('current')
ciurOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 191, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciurOperStatus.setStatus('current')
ciscoIpUplinkRedirectMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 2))
ciscoIpUplinkRedirectMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3))
ciscoIpUplinkRedirectMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1))
ciscoIpUplinkRedirectMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2))
ciscoIpUplinkRedirectMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 1, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciscoIpUplinkRedirectMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBCompliance = ciscoIpUplinkRedirectMIBCompliance.setStatus('current')
ciscoIpUplinkRedirectMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 191, 3, 2, 1)).setObjects(("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurStartupStatus"), ("CISCO-IP-UPLINK-REDIRECT-MIB", "ciurOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpUplinkRedirectMIBGroup = ciscoIpUplinkRedirectMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IP-UPLINK-REDIRECT-MIB", ciurStartupStatus=ciurStartupStatus, ciscoIpUplinkRedirectMIBGroup=ciscoIpUplinkRedirectMIBGroup, ciscoIpUplinkRedirectMIB=ciscoIpUplinkRedirectMIB, ciscoIpUplinkRedirectMIBCompliances=ciscoIpUplinkRedirectMIBCompliances, ciscoIpUplinkRedirectMIBNotificationPrefix=ciscoIpUplinkRedirectMIBNotificationPrefix, ciscoIpUplinkRedirectMIBCompliance=ciscoIpUplinkRedirectMIBCompliance, ciurOperStatus=ciurOperStatus, ciscoIpUplinkRedirectMIBGroups=ciscoIpUplinkRedirectMIBGroups, ciscoIpUplinkRedirectMIBObjects=ciscoIpUplinkRedirectMIBObjects, ciscoIpUplinkRedirectMIBConformance=ciscoIpUplinkRedirectMIBConformance, PYSNMP_MODULE_ID=ciscoIpUplinkRedirectMIB)
