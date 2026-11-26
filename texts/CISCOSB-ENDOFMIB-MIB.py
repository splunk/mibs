#
# PySNMP MIB module CISCOSB-ENDOFMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-ENDOFMIB-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rndEndOfMibGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1000))
rndEndOfMibGroup.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rndEndOfMibGroup.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rndEndOfMibGroup.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rndEndOfMibGroup.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rndEndOfMibGroup.setContactInfo('Postal: 170 West Tasman Drive\n                San Jose , CA 95134-1706\n                USA\n\n                \n                Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rndEndOfMibGroup.setDescription('This private MIB module defines End of MIB private MIBs.')
rndEndOfMib = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 1000, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rndEndOfMib.setStatus('current')
if mibBuilder.loadTexts: rndEndOfMib.setDescription(' This variable indicates this is the end of switch001 MIB.')
mibBuilder.exportSymbols("CISCOSB-ENDOFMIB-MIB", rndEndOfMib=rndEndOfMib, PYSNMP_MODULE_ID=rndEndOfMibGroup, rndEndOfMibGroup=rndEndOfMibGroup)
