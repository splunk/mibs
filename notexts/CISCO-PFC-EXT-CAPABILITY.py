#
# PySNMP MIB module CISCO-PFC-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PFC-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPfcExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 626))
ciscoPfcExtCapability.setRevisions(('2014-08-11 00:00',))
if mibBuilder.loadTexts: ciscoPfcExtCapability.setLastUpdated('201408110000Z')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setOrganization('Cisco Systems, Inc.')
cpeCapNxOSV06R0002U0201PN3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 626, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus \n                        3000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setStatus('current')
mibBuilder.exportSymbols("CISCO-PFC-EXT-CAPABILITY", ciscoPfcExtCapability=ciscoPfcExtCapability, PYSNMP_MODULE_ID=ciscoPfcExtCapability, cpeCapNxOSV06R0002U0201PN3k=cpeCapNxOSV06R0002U0201PN3k)
