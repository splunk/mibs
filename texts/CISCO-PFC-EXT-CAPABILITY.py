#
# PySNMP MIB module CISCO-PFC-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PFC-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPfcExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 626))
ciscoPfcExtCapability.setRevisions(('2014-08-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPfcExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPfcExtCapability.setLastUpdated('201408110000Z')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPfcExtCapability.setDescription('The capabilities description of CISCO-PFC-EXT-MIB.')
cpeCapNxOSV06R0002U0201PN3k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 626, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setProductRelease('Cisco NX-OS 6.0(2)U2(1) on Nexus \n                        3000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cpeCapNxOSV06R0002U0201PN3k = cpeCapNxOSV06R0002U0201PN3k.setStatus('current')
if mibBuilder.loadTexts: cpeCapNxOSV06R0002U0201PN3k.setDescription('CISCO-PFC-EXT-MIB agent capabilities.')
mibBuilder.exportSymbols("CISCO-PFC-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoPfcExtCapability, ciscoPfcExtCapability=ciscoPfcExtCapability, cpeCapNxOSV06R0002U0201PN3k=cpeCapNxOSV06R0002U0201PN3k)
