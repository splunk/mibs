#
# PySNMP MIB module CISCO-BITS-CLOCK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-BITS-CLOCK-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBitsClockCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 433))
ciscoBitsClockCapability.setRevisions(('2005-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoBitsClockCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoBitsClockCapability.setLastUpdated('200503080000Z')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setContactInfo('       Cisco Systems\n                                Customer Service\n                        \n                        Postal: 170 West Tasman Drive\n                                San Jose, CA  95134\n                                USA\n                        \n                           Tel: +1 800 553-NETS\n                        \n                        E-mail: cs-ss7@cisco.com')
if mibBuilder.loadTexts: ciscoBitsClockCapability.setDescription('Agent capabilities for the CISCO-BITS-CLOCK-MIB.')
ciscoBitsClockV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 433, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBitsClockV12R025000SW1 = ciscoBitsClockV12R025000SW1.setStatus('current')
if mibBuilder.loadTexts: ciscoBitsClockV12R025000SW1.setDescription('IOS 12.2(25)SW1 Cisco CISCO-BITS-CLOCK-MIB.my \n                   User Agent MIB capabilities.')
mibBuilder.exportSymbols("CISCO-BITS-CLOCK-CAPABILITY", ciscoBitsClockCapability=ciscoBitsClockCapability, PYSNMP_MODULE_ID=ciscoBitsClockCapability, ciscoBitsClockV12R025000SW1=ciscoBitsClockV12R025000SW1)
