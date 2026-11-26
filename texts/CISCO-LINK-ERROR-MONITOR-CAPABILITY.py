#
# PySNMP MIB module CISCO-LINK-ERROR-MONITOR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LINK-ERROR-MONITOR-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLinkErrorMonitorCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 414))
ciscoLinkErrorMonitorCapability.setRevisions(('2004-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setLastUpdated('200408050000Z')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoLinkErrorMonitorCapability.setDescription('This MIB module describes the capability \n                 of CISCO-LINK-ERROR-MONITOR-MIB.')
clemCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 414, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clemCapCatOSV08R0401 = clemCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: clemCapCatOSV08R0401.setDescription('CISCO-LINK-ERROR-MONITOR-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-LINK-ERROR-MONITOR-CAPABILITY", clemCapCatOSV08R0401=clemCapCatOSV08R0401, PYSNMP_MODULE_ID=ciscoLinkErrorMonitorCapability, ciscoLinkErrorMonitorCapability=ciscoLinkErrorMonitorCapability)
