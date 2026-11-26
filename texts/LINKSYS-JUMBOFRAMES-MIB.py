#
# PySNMP MIB module LINKSYS-JUMBOFRAMES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-JUMBOFRAMES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:12:02 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, Gauge32, Unsigned32, NotificationType, iso, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, MibIdentifier, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "iso", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "MibIdentifier", "IpAddress", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlJumboFrames = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91))
rlJumboFrames.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlJumboFrames.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlJumboFrames.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlJumboFrames.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlJumboFrames.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlJumboFrames.setDescription('This private MIB module defines Jumbo Frames private MIBs.')
rlJumboFramesCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesCurrentStatus.setDescription('Show the current Jumbo Frames status')
rlJumboFramesStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 91, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlJumboFramesStatusAfterReset.setDescription('Set the Jumbo Frames status after reset')
mibBuilder.exportSymbols("LINKSYS-JUMBOFRAMES-MIB", rlJumboFramesStatusAfterReset=rlJumboFramesStatusAfterReset, PYSNMP_MODULE_ID=rlJumboFrames, rlJumboFramesCurrentStatus=rlJumboFramesCurrentStatus, rlJumboFrames=rlJumboFrames)
